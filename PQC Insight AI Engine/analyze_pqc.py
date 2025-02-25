import pandas as pd
import pickle
import json

# Load training data
df = pd.read_csv("pqc_training_data.csv")

# Ensure PQC Compatible is treated as a boolean
df["PQC Compatible"] = df["PQC Compatible"].astype(str).str.strip().map(lambda x: x.lower() in ["yes", "true", "1"])

# Load trained model & encoders
with open("pqc_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("label_encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

def analyze_environment(os_type, crypto_lib, web_server, cert_type):
    """
    1. Check if the server setup exists in training data.
    2. If found, return stored compatibility info.
    3. Otherwise, use AI to predict.
    """

    # 1️⃣ **Check if this exact setup is already in training data**
    match = df[
        (df["OS Type"] == os_type) & 
        (df["Crypto Library"] == crypto_lib) & 
        (df["Web Server"] == web_server) & 
        (df["Cert Type"] == cert_type)
    ]
    
    if not match.empty:
        # ✅ **Found in training data! Read compatibility correctly**
        pqc_compatible = match["PQC Compatible"].values[0]  # This is now a True/False value
        recommended_pqc = match["Best PQC Algorithm"].values[0]
        upgrade_steps = match["Upgrade Steps"].values[0]

        result = {
            "server": "example.com",
            "os": os_type,
            "pqc_compatibility": "Yes" if pqc_compatible else "No",
            "recommended_pqc_algorithm": recommended_pqc,
            "steps_to_enable_pqc": upgrade_steps.split("; ") if not pqc_compatible else [],
            "reason": "Found in training data"
        }
        return json.dumps(result, indent=4)

    # 2️⃣ **Not found? Use AI to predict**
    input_data = pd.DataFrame([[os_type, crypto_lib, web_server, cert_type]], 
                              columns=["OS Type", "Crypto Library", "Web Server", "Cert Type"])

    # 3️⃣ **Encode input values**
    try:
        for col in input_data.columns:
            input_data[col] = encoders[col].transform(input_data[col])
    except ValueError as e:
        return f"Error: Unknown value in input - {e}"

    # 4️⃣ **Use AI model to predict compatibility**
    pqc_compatible = model.predict(input_data)[0]
    recommended_pqc = "CRYSTALS-DILITHIUM" if pqc_compatible else "Falcon"
    upgrade_steps = "Upgrade OpenSSL to v3.0; Modify Apache config" if not pqc_compatible else "None"

    # 5️⃣ **Return AI-generated recommendation**
    result = {
        "server": "example.com",
        "os": os_type,
        "pqc_compatibility": "Yes" if pqc_compatible else "No",
        "recommended_pqc_algorithm": recommended_pqc,
        "steps_to_enable_pqc": upgrade_steps.split("; ") if not pqc_compatible else [],
        "reason": "Predicted using AI (not found in training data)"
    }
    return json.dumps(result, indent=4)

# Example Usage
print(analyze_environment("Ubuntu 20.04", "OpenSSL 1.1.1", "Apache", "RSA-2048"))

