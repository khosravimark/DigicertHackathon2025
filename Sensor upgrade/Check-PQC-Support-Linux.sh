#!/bin/bash

SERVER=${1:-"example.com"}
PORT=${2:-443}

# List of known PQC algorithms
PQC_ALGORITHMS=("CRYSTALS-Kyber" "Dilithium" "Falcon" "SPHINCS+")

# Function to get the certificate details
get_certificate_info() {
    echo "[*] Fetching certificate from $SERVER:$PORT..."
    CERT_INFO=$(echo | openssl s_client -connect $SERVER:$PORT -servername $SERVER 2>/dev/null | openssl x509 -noout -text)
    
    if [[ -z "$CERT_INFO" ]]; then
        echo "[-] Failed to retrieve certificate."
        exit 1
    fi

    echo "$CERT_INFO"
}

# Function to check if the certificate uses PQC
check_certificate_for_pqc() {
    CERT_INFO="$1"
    
    echo "[*] Checking certificate algorithm..."
    for ALG in "${PQC_ALGORITHMS[@]}"; do
        if echo "$CERT_INFO" | grep -iq "$ALG"; then
            echo "[+] Server is using a PQC algorithm: $ALG"
            return 0
        fi
    done

    echo "[-] No PQC algorithm detected in the certificate."
}

# Function to check for PQC cipher suites
check_tls_ciphers() {
    echo "[*] Checking TLS cipher suites..."
    TLS_CIPHERS=$(openssl s_client -connect $SERVER:$PORT -cipher ALL 2>&1 | grep -E "TLS|Cipher")

    if [[ -z "$TLS_CIPHERS" ]]; then
        echo "[-] Failed to retrieve TLS cipher suites."
        return 1
    fi

    echo "$TLS_CIPHERS" | while read -r line; do
        for ALG in "${PQC_ALGORITHMS[@]}"; do
            if echo "$line" | grep -iq "$ALG"; then
                echo "[+] Server supports PQC Cipher Suite: $ALG"
                return 0
            fi
        done
    done

    echo "[-] No PQC cipher suites detected."
}

# Main execution
CERT_INFO=$(get_certificate_info)
check_certificate_for_pqc "$CERT_INFO"
check_tls_ciphers

