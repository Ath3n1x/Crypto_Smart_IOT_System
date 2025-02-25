from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Example model update to be encrypted
model_update = "Device 1 model weights: [0.2, 0.4, 0.6]"

# Generate a symmetric key
symmetric_key = get_random_bytes(16)  # AES key length 16 bytes (128-bit)
cipher = AES.new(symmetric_key, AES.MODE_EAX)

# Encrypt the model update
ciphertext, tag = cipher.encrypt_and_digest(model_update.encode())

print("Encrypted Model Update:", ciphertext.hex())

# Decrypt the model update (server-side)
cipher_dec = AES.new(symmetric_key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_data = cipher_dec.decrypt(ciphertext)

print("Decrypted Model Update:", decrypted_data.decode())

