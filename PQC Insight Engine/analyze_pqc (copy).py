import pandas as pd
import pickle
import json

# Load trained model & encoders
with open("pqc_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("label_encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

def analyze_environment(os_type, crypto_lib, web_server, cert_type):
    input_data = pd.DataFrame([[os_type, crypto_lib, web_server, cert_type]], 
                              columns=["OS Type", "Crypto Library", "Web Server", "Cert Type"])

    print("Input Data Before Encoding:", input_data)  # Debugging line

    # Encode input safely
    for col in input_data.columns:
        if input_data[col][0] not in encoders[col].classes_:
            return f"Error: '{input_data[col][0]}' not found in trained data for '{col}'. Available values: {encoders[col].classes_}"
        input_data[col] = encoders[col].transform(input_data[col])

    print("Encoded Input:", input_data)  # Debugging line


    # Predict PQC Compatibility
    pqc_compatible = model.predict(input_data)[0]

    # Get Recommended PQC Algorithm
    recommended_pqc = "CRYSTALS-DILITHIUM" if pqc_compatible else "Falcon"

    # Get Upgrade Steps if not compatible
    upgrade_steps = "Upgrade OpenSSL to v3.0; Modify Apache config" if not pqc_compatible else "None"

    # Generate JSON Response
    result = {
        "server": "example.com",
        "os": os_type,
        "pqc_compatibility": "Yes" if pqc_compatible else "No",
        "recommended_pqc_algorithm": recommended_pqc,
        "steps_to_enable_pqc": upgrade_steps if not pqc_compatible else []
    }

    return json.dumps(result, indent=4)

# Example Usage
print(analyze_environment("Ubuntu 20.04", "OpenSSL 1.1.1", "Apache", "RSA-2048"))

