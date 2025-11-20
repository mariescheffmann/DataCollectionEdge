# DataCollectionCloud

## Windows Powershell
mkdir certs
copy "path\to\Cloud\secrets\certs\ca.crt" certs/ca.crt

cd certs

# Generate private key and CSR (Certificate Signing Request)
openssl req -new -newkey rsa:2048 -nodes -keyout client.key -out client.csr -subj "/CN=edge-client"

# Sign certifikate with Cloud CA
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365



## For mac

mkdir -p certs
cp /path/to/DataCollectionCloud/secrets/certs/ca.crt certs/ca.crt


cd certs

# Generate private key and CSR (Certificate Signing Request)
openssl req -new -newkey rsa:2048 -nodes -keyout client.key -out client.csr -subj "/CN=edge-client"

# Sign certifikate with Cloud CA
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
