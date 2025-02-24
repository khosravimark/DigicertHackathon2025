PQC Detection Scripts
Overview
The dc1 system currently scans for existing certificates, but it should be upgraded using these scripts to also determine whether a server supports Post-Quantum Cryptography (PQC). These scripts identify:

Whether the server’s SSL/TLS certificate is using a PQC algorithm.
Whether the server’s TLS handshake supports PQC cipher suites.
This information will be used by the PQC Insight AI Engine to analyze compatibility and provide recommendations on how to make the server PQC-enabled.

Scripts
PowerShell Script (check_pqc.ps1) – For Windows systems
Bash Script (check_pqc.sh) – For Linux servers
Both scripts perform the following checks:
✅ Extracts the SSL certificate from the specified server and port.
✅ Identifies the public key algorithm (RSA, ECC, or PQC).
✅ Scans TLS cipher suites for PQC support (Kyber, Dilithium, Falcon, SPHINCS+).
✅ Provides a report on PQC readiness.

Installation & Usage
Windows (PowerShell)
Open PowerShell and run:
powershell
Copy
Edit
Set-ExecutionPolicy Unrestricted -Scope Process -Force
Run the script:
powershell
Copy
Edit
.\check_pqc.ps1 -Server yourserver.com -Port 443
Linux (Bash)
Make the script executable:
bash
Copy
Edit
chmod +x check_pqc.sh
Run the script:
bash
Copy
Edit
./check_pqc.sh yourserver.com 443
Next Steps
Integrate this script into dc1 for automated PQC readiness checks.
Feed the output into the PQC Insight AI Engine for migration recommendations.
Use the insights to transition your environment towards PQC security with minimal downtime.
🚀 Future-proof your infrastructure with PQC detection and AI-driven migration strategies!
