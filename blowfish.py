from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Blowfish block size is 8 bytes
BLOCK_SIZE = Blowfish.block_size

# Key must be between 4 and 56 bytes
key = b'SecretKey'  # example key

# Create cipher object with random IV
iv = get_random_bytes(BLOCK_SIZE)
cipher_encrypt = Blowfish.new(key, Blowfish.MODE_CBC, iv)

# Message to encrypt
data = b'confidential Information'
padded_data = pad(data, BLOCK_SIZE)

# Encrypt
encrypted_data = cipher_encrypt.encrypt(padded_data)

print("Encrypted (hex):", encrypted_data.hex())

# Decryption
cipher_decrypt = Blowfish.new(key, Blowfish.MODE_CBC, iv)
decrypted_padded_data = cipher_decrypt.decrypt(encrypted_data)
decrypted_data = unpad(decrypted_padded_data, BLOCK_SIZE)

print("Decrypted:", decrypted_data.decode())
