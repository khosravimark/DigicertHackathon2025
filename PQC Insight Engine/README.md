# PQC Insight AI Engine

## 🔍 Overview
The **PQC Insight AI Engine** is an AI-powered tool designed to analyze server environments and determine their **compatibility with Post-Quantum Cryptography (PQC)**. It assesses cryptographic libraries, certificate types, and TLS configurations to:

- Identify whether a server currently supports **PQC algorithms**.
- Recommend the **best PQC algorithm** based on the detected environment.
- Provide **step-by-step guidance** on enabling PQC if the server is not yet compatible.

## 🚀 Features
✔ **Scans servers** for TLS settings, certificates, and crypto libraries.  
✔ **Uses AI** to predict **PQC readiness** based on historical data.  
✔ **Recommends migration steps** for non-compatible environments.  
✔ **Integrates with existing security tools** to automate PQC assessment.  
✔ Outputs structured **JSON reports** for easy integration with security systems.  

## 🛠 Integration with Scanning Solutions
The AI engine integrates with **TLS scanning tools** and **certificate management platforms** to provide real-time insights.

### 📡 Components & Workflow
1️⃣ **Scanning Module** (`scan_pqc_support.py`)  
   - Performs server analysis via **TLS handshake** and **certificate parsing**.  
   - Extracts cryptographic details (e.g., OpenSSL version, certificate type).  

2️⃣ **AI Analysis Module** (`pqc_analyze.py`)  
   - Uses **machine learning** to predict PQC compatibility.  
   - Matches results against a **training dataset** of known server configurations.  

3️⃣ **JSON Report Generator**  
   - Outputs structured data indicating PQC readiness, recommended algorithms, and migration steps.  

## 📂 Project Structure
```
📦 PQC_Insight_AI
├── 📜 scan_pqc_support.py  # Scans TLS certificates & cryptographic stack
├── 📜 pqc_analyze.py        # AI engine for PQC readiness analysis
├── 📜 train_model.py        # Model training script
├── 📜 dataset.csv           # Training dataset for PQC support
├── 📜 requirements.txt      # Required dependencies
├── 📜 README.md             # Project documentation
└── 📜 config.json           # Configuration file for integration
```

## 📊 Training Dataset (`dataset.csv`)
The dataset contains historical information on server configurations, cryptographic libraries, and PQC support.

### Example Data Structure:
| OS Type       | Crypto Library | Web Server | Cert Type  | PQC Compatible | Recommended Algorithm | Steps to Enable PQC |
|--------------|---------------|------------|------------|----------------|------------------------|----------------------|
| Ubuntu 20.04 | OpenSSL 1.1.1 | Apache     | RSA-2048   | No             | CRYSTALS-DILITHIUM     | Upgrade OpenSSL 3.0 |
| Windows      | Schannel      | IIS        | ECDSA      | No             | -                      | Use OpenSSL Wrapper |
| Ubuntu 22.04 | OpenSSL 3.0   | Nginx      | RSA-3072   | Yes            | Falcon                 | -                    |

## 📚 Training the AI Model (`train_model.py`)
The AI model is trained using historical server configurations and cryptographic settings.

### Steps to Train the Model:
1. Ensure `dataset.csv` is up-to-date with recent PQC adoption trends.
2. Run the training script:
   ```sh
   python train_model.py
   ```
3. The model learns patterns and predicts PQC compatibility for new servers.
4. Save the trained model (`pqc_model.pkl`) for use in analysis.

## 📌 Running the PQC Analysis (`pqc_analyze.py`)
To analyze a new server for PQC support, run:
```sh
python pqc_analyze.py --server example.com --port 443
```
### Example Output (Server NOT PQC Ready)
```json
{
    "server": "example.com",
    "crypto_library": "OpenSSL 1.1.1",
    "pqc_supported": "No",
    "recommended_pqc_algorithm": "CRYSTALS-DILITHIUM",
    "steps_to_enable_pqc": ["Upgrade OpenSSL to 3.0"]
}
```
### Example Output (Server PQC Ready)
```json
{
    "server": "pqctest.com",
    "crypto_library": "OpenSSL 3.0+",
    "pqc_supported": "Yes",
    "recommended_pqc_algorithm": "Falcon",
    "steps_to_enable_pqc": []
}
```

## 🔗 Future Enhancements
✅ **Expand AI dataset** with real-world PQC-supported servers.  
✅ **Integrate with DigiCert APIs** for real-time certificate insights.  
✅ **Automate remediation** for non-PQC-compatible servers.  

## 💡 Conclusion
The **PQC Insight AI Engine** is a powerful solution for **post-quantum cryptography readiness assessment**. It provides actionable intelligence, ensuring **future-proof security** in enterprise environments.

🔐 **Stay ahead of quantum threats – deploy PQC today!** 🚀

## 📬 Questions? Contributions?
Feel free to reach out or submit issues via GitHub! 🚀


