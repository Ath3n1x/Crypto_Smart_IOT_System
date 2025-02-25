from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Load RSA private key
with open("private_key.pem", "r") as key_file:
    private_key = RSA.import_key(key_file.read())

# Create a digital signature
model_update = "Device 1 model weights: [0.2, 0.4, 0.6]"
hashed_update = SHA256.new(model_update.encode())
signature = pkcs1_15.new(private_key).sign(hashed_update)

print(f"Digital Signature: {signature.hex()}")

