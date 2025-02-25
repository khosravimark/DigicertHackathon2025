# PQC Insight AI Engine - DC1 Integration

## 🚀 Overview
The **PQC Insight AI Engine** is designed to integrate with **DigiCert DC1** to provide **Post-Quantum Cryptography (PQC) readiness assessments** for discovered certificates. The solution enhances the DC1 platform by analyzing certificate environments, recommending the best PQC algorithms, and providing step-by-step guidance for enabling PQC support.

### 🌍 Solution Components
This project consists of three main components:

1️⃣ **Sensor Upgrades** (`sensor_upgrades/`)
   - Enhancements to the **DC1 Sensor** to collect PQC support data.
   - Extracts cryptographic libraries and environment details.
   - Sends PQC-relevant data to DC1 for AI-based analysis.

2️⃣ **PQC Insight AI Engine** (`pqc_insight_ai_engine/`)
   - AI-driven analysis of PQC compatibility.
   - Trained model determines if a server is PQC-ready.
   - Provides recommendations and upgrade instructions.
   - Exposes results via an API for integration with DC1.

3️⃣ **DC1 Integration** (`dc1_integration/`)
   - Adds a **PQC Insight** tab to discovered certificates in DC1.
   - Displays PQC compatibility, upgrade steps, and recommended algorithms.
   - Future roadmap includes automation to assist with PQC transitions.

## 🛠 How It Works
### 🔍 **Step 1: Network Scanning with Sensor Upgrades**
- The **DC1 Sensor** scans the network and collects **certificate & cryptographic data**.
- New enhancements allow it to detect PQC support indicators (e.g., OpenSSL 3.0+, Falcon, Dilithium support).
- Data is forwarded to **DC1 for processing**.

### 🤖 **Step 2: AI-Based PQC Analysis**
- The **PQC Insight AI Engine** processes the discovered certificates.
- It uses machine learning models to:
  - Determine **PQC compatibility**.
  - Recommend the best PQC algorithm.
  - Provide **step-by-step instructions** for enabling PQC.
- The AI model is continuously updated to reflect industry trends.

### 📊 **Step 3: Displaying Insights in DC1**
- A new **PQC Insight** tab is added to each discovered certificate in DC1.
- Users can view:
  - **PQC Readiness Status** (Yes/No)
  - **Recommended PQC Algorithm** (e.g., Dilithium, Falcon)
  - **Steps to Enable PQC** (if needed)

### 🚀 **Step 4: Future Automation**
- The long-term goal is to **automate the PQC transition process**.
- DC1 will provide upgrade guidance and eventually **automate cryptographic migration**.

## 📂 Project Structure
```
📦 PQC_DC1_Integration
├── 📁 sensor_upgrades        # Enhancements for DC1 Sensor
│   ├── capture_pqc_data.py  # Script to extract PQC support info
│   ├── sensor_config.json   # Sensor configuration updates
│   ├── README.md            # Sensor documentation
│
├── 📁 pqc_insight_ai_engine  # AI-powered PQC analysis
│   ├── train_model.py       # AI model training script
│   ├── pqc_analyze.py       # AI analysis script
│   ├── api.py               # API for PQC assessment
│   ├── dataset.csv          # Training dataset
│   ├── README.md            # AI Engine documentation
│
├── 📁 dc1_integration        # DC1 UI enhancements
│   ├── static_ui.html       # Mockup of PQC Insight tab in DC1
│   ├── integration_notes.md # Steps to integrate with DC1
│   ├── README.md            # DC1 UI documentation
│
├── requirements.txt         # Dependencies for the AI engine
├── README.md                # Main project documentation
└── config.json              # Configuration file
```

## 📌 Running the PQC Insight AI Engine
To train the model:
```sh
python pqc_insight_ai_engine/train_model.py
```
To analyze a specific certificate environment:
```sh
python pqc_insight_ai_engine/pqc_analyze.py --os "Ubuntu 20.04" --crypto "OpenSSL 1.1.1" --cert "RSA-2048"
```
To expose an API endpoint:
```sh
python pqc_insight_ai_engine/api.py
```

## 🔗 Future Enhancements
✅ **Automate PQC transitions via DC1 API**  
✅ **Improve AI model with real-world adoption data**  
✅ **Expand compatibility detection for more cryptographic libraries**  

## 💡 Conclusion
The **PQC Insight AI Engine** seamlessly integrates into **DigiCert DC1** to provide **AI-powered PQC readiness insights**. With this solution, organizations can prepare for the **post-quantum cryptographic era**, ensuring a **secure, future-proof infrastructure**.

🔐 **Stay ahead of quantum threats with PQC Insight AI!** 🚀

## 📬 Questions? Contributions?
Feel free to reach out or submit issues via GitHub! 🚀


