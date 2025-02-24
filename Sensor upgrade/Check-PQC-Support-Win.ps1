# Requires PowerShell 7+ for TLS checks
param (
    [string]$Server = "example.com",
    [int]$Port = 443
)

function Get-CertificateDetails {
    param ($Server, $Port)

    try {
        $tcpClient = New-Object System.Net.Sockets.TcpClient
        $tcpClient.Connect($Server, $Port)
        $sslStream = New-Object System.Net.Security.SslStream($tcpClient.GetStream(), $false, ({ $true } -as [System.Net.Security.RemoteCertificateValidationCallback]))
        $sslStream.AuthenticateAsClient($Server)

        $cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($sslStream.RemoteCertificate)
        $sslStream.Dispose()
        $tcpClient.Close()

        return $cert
    }
    catch {
        Write-Host "Failed to retrieve the certificate: $_"
        return $null
    }
}

function Get-SupportedCipherSuites {
    try {
        $tlsCiphers = openssl s_client -connect "$Server`:$Port" -cipher ALL 2>&1 | Select-String -Pattern "Cipher" -Context 0,1
        return $tlsCiphers -match "TLS" -or $tlsCiphers -match "PQC"
    }
    catch {
        Write-Host "Could not retrieve TLS cipher suites."
        return $null
    }
}

function Check-PQC {
    param ($cert, $tlsCiphers)

    $pqcAlgorithms = @("CRYSTALS-Kyber", "Dilithium", "Falcon", "SPHINCS+")
    $isPQC = $false

    # Check the certificate's public key algorithm
    if ($cert) {
        Write-Host "Certificate Subject: $($cert.Subject)"
        Write-Host "Issuer: $($cert.Issuer)"
        Write-Host "Algorithm: $($cert.SignatureAlgorithm.FriendlyName)"

        foreach ($alg in $pqcAlgorithms) {
            if ($cert.SignatureAlgorithm.FriendlyName -match $alg) {
                $isPQC = $true
                Write-Host "[+] Server is using a PQC algorithm: $alg"
                break
            }
        }
    }

    # Check TLS Cipher Suites for PQC support
    if ($tlsCiphers) {
        foreach ($alg in $pqcAlgorithms) {
            if ($tlsCiphers -match $alg) {
                $isPQC = $true
                Write-Host "[+] Server supports PQC Cipher Suite: $alg"
            }
        }
    }

    if (-not $isPQC) {
        Write-Host "[-] No PQC support detected. The server may still be using RSA or ECC."
    }
}

# Main execution
$cert = Get-CertificateDetails -Server $Server -Port $Port
$tlsCiphers = Get-SupportedCipherSuites
Check-PQC -cert $cert -tlsCiphers $tlsCiphers

