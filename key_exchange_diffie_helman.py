from Crypto.PublicKey import DSA
from Crypto.Random import random
from hashlib import sha256

# Generate Diffie-Hellman private and public keys
private_key = random.StrongRandom().randint(1, 2**256)
base, prime = 2, 23  # Example parameters

public_key = pow(base, private_key, prime)

# Simulate server's public key
server_private_key = random.StrongRandom().randint(1, 2**256)
server_public_key = pow(base, server_private_key, prime)

# Compute shared secret
shared_secret = pow(server_public_key, private_key, prime)
aes_key = sha256(str(shared_secret).encode()).digest()[:16]

print("Shared AES Key:", aes_key.hex())

