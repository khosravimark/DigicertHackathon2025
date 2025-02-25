# PQC Insight AI Engine

## 🔍 Overview
The **PQC Insight AI Engine** is an AI-powered tool designed to analyze server environments and determine their **compatibility with Post-Quantum Cryptography (PQC)**. It utilizes machine learning models trained on historical cryptographic data to:

- Identify whether a server currently supports **PQC algorithms**.
- Recommend the **best PQC algorithm** based on detected configurations.
- Provide **steps to enable PQC** if the server is not yet compatible.

## 🚀 Features
✔ **AI-driven PQC compatibility assessment**  
✔ **Model trained on historical cryptographic data**  
✔ **Recommends optimal PQC algorithms**  
✔ **Provides steps to enable PQC where needed**  
✔ **Outputs structured JSON results**  

## 📡 Components & Workflow

1️⃣ **Training Module** (`train_model.py`)  
   - Processes `dataset.csv` to train a model on cryptographic environments.  
   - Uses machine learning to understand patterns in PQC compatibility.  

2️⃣ **AI Analysis Module** (`pqc_analyze.py`)  
   - Takes input parameters (OS type, crypto library, certificate type).  
   - Uses the trained model to determine PQC compatibility and recommend an algorithm.  

3️⃣ **API Module** (`api.py`)  
   - Provides a REST API for querying PQC compatibility analysis.  
   - Accepts structured input and returns JSON-formatted results.  

## 📂 Project Structure
```
📦 PQC_Insight_AI
├── 📜 train_model.py        # Model training script
├── 📜 pqc_analyze.py        # AI-based PQC analysis
├── 📜 api.py                # API for PQC assessment
├── 📜 dataset.csv           # Training dataset
├── 📜 requirements.txt      # Required dependencies
├── 📜 README.md             # Project documentation
└── 📜 config.json           # Configuration file
```

## 📊 Training Dataset (`dataset.csv`)
The dataset contains cryptographic configurations, OS details, and PQC compatibility indicators.

### Example Data Structure:
| OS Type       | Crypto Library | Cert Type  | PQC Compatible | Recommended Algorithm | Steps to Enable PQC |
|--------------|---------------|------------|----------------|------------------------|----------------------|
| Ubuntu 20.04 | OpenSSL 1.1.1 | RSA-2048   | No             | CRYSTALS-DILITHIUM     | Upgrade OpenSSL 3.0 |
| Windows      | Schannel      | ECDSA      | No             | -                      | Use OpenSSL Wrapper |
| Ubuntu 22.04 | OpenSSL 3.0   | RSA-3072   | Yes            | Falcon                 | -                    |

## 📚 Training the AI Model (`train_model.py`)
The AI model is trained using historical cryptographic environments.

### Steps to Train the Model:
1. Ensure `dataset.csv` is up-to-date with recent PQC adoption trends.
2. Run the training script:
   ```sh
   python train_model.py
   ```
3. The model learns compatibility patterns and saves a trained model (`pqc_model.pkl`).

## 📌 Running the PQC Analysis (`pqc_analyze.py`)
To analyze PQC support for a given environment, run:
```sh
python pqc_analyze.py --os "Ubuntu 20.04" --crypto "OpenSSL 1.1.1" --cert "RSA-2048"
```
### Example Output (Not PQC Ready)
```json
{
    "os": "Ubuntu 20.04",
    "crypto_library": "OpenSSL 1.1.1",
    "pqc_supported": "No",
    "recommended_pqc_algorithm": "CRYSTALS-DILITHIUM",
    "steps_to_enable_pqc": ["Upgrade OpenSSL to 3.0"]
}
```
### Example Output (PQC Ready)
```json
{
    "os": "Ubuntu 22.04",
    "crypto_library": "OpenSSL 3.0+",
    "pqc_supported": "Yes",
    "recommended_pqc_algorithm": "Falcon",
    "steps_to_enable_pqc": []
}
```

## 📌 Running the API (`api.py`)
To query the AI engine via API, run:
```sh
python api.py
```
Then, send a request:
```sh
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"os": "Ubuntu 20.04", "crypto_library": "OpenSSL 1.1.1", "cert_type": "RSA-2048"}'
```
### Example API Response
```json
{
    "pqc_supported": "No",
    "recommended_pqc_algorithm": "CRYSTALS-DILITHIUM",
    "steps_to_enable_pqc": ["Upgrade OpenSSL to 3.0"]
}
```

## 🔗 Future Enhancements
✅ **Expand AI dataset** with real-world PQC adoption data.  
✅ **Integrate with automated security platforms**.  
✅ **Enhance AI model for dynamic PQC migration recommendations**.  

## 💡 Conclusion
The **PQC Insight AI Engine** is a powerful tool for **post-quantum cryptography readiness assessment**. It provides AI-driven insights for organizations transitioning to **quantum-safe cryptographic environments**.

🔐 **Secure your future today with PQC Insight AI!** 🚀

## 📬 Questions? Contributions?
Feel free to reach out or submit issues via GitHub! 🚀


