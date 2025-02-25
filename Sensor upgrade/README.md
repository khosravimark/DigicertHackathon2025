# PQC Detection Scripts

## Overview

The **dc1** system currently scans for existing certificates, but it should be upgraded using these scripts to also determine whether a server supports Post-Quantum Cryptography (PQC). These scripts identify:

- Whether the server’s SSL/TLS certificate is using a PQC algorithm.
- Whether the server’s TLS handshake supports PQC cipher suites.

This information will be used by the **PQC Insight AI Engine** to analyze compatibility and provide recommendations on how to make the server PQC-enabled.

## Scripts

- **PowerShell Script (`Check-PQC-Support-Win.ps1`)** – For Windows systems  
- **Bash Script (`Check-PQC-Support-Linux.sh`)** – For Linux servers  

### Features

✅ Extracts the SSL certificate from the specified server and port.  
✅ Identifies the public key algorithm (RSA, ECC, or PQC).  
✅ Scans TLS cipher suites for PQC support (Kyber, Dilithium, Falcon, SPHINCS+).  
✅ Provides a report on PQC readiness.

## Installation & Usage

### Windows (PowerShell)

1. Open PowerShell and run:  
   ```powershell
   Set-ExecutionPolicy Unrestricted -Scope Process -Force
   
2. Run the script:

   .\Check-PQC-Support-Win.ps1 -Server yourserver.com -Port 443
   
### Linux (Bash)

1. Make the script executable:
	```bash
	chmod +x check_pqc.sh
2. Run the script:

        ./Check-PQC-Support-Linux.sh yourserver.com 443
        
##  Next Steps

Integrate this script into dc1 for automated PQC readiness checks.
Feed the output into the PQC Insight AI Engine for migration recommendations.
Use the insights to transition your environment towards PQC security with minimal downtime.

### 🚀 Future-proof your infrastructure with PQC detection and AI-driven migration strategies!
