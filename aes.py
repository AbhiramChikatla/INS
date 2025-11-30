from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

plaintext = b"Hello Adavanced Encryption Standard"
print("original msg:",plaintext)

# Key and IV (16 bytes each for AES-128)
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Encode ciphertext for display
print("Encrypted (base64):", base64.b64encode(ciphertext).decode())

# Decrypt
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

print("Decrypted:", decrypted.decode())






# AES is a block cipher intended to replace DES for commercial applications. It uses a 128-bit block size and a key size of 128, 192, or 256 bits.
#  AES does not use a Feistel structure. Instead, each full round consists of four separate functions: byte substitution, permutation, arithmetic opera- tions over a finite field, and XOR with a key.
# The cipher takes a plaintext block size of 128 bits, or 16 bytes. The key length can be 16(10 rounds), 24(12 rounds), or 32(14 rounds) bytes (128, 192, or 256 bits). The algorithm is referred to as AES-128, AES-192, or AES-256, depending on the key length.



# Overview of AES
# Block size -128 bit plain text(4word/16 bytes):1 word =32 bits
# NO.of rounds:10
# Key size:128 bit(4word/16 bytes)
# No.of subkeys-44 sub keys
# Each subkey size-32 bits(1 word/4 bytes)
# Each round using-4 sub keys(4 words/16 bytes/128 bits)
# Pre round condition-4 sub key
# Cipher text-128 bits(4 words/16 bytes)


# Four different stages are used, one of permutation and three of substitution:
# • Substitute bytes: Uses an S-box to perform a byte-by-byte substitution of the block
# • ShiftRows: A simple permutation
# • MixColumns: A substitution that makes use of arithmetic over
# • AddRoundKey: A simple bitwise XOR of the current block with a portion of the expanded key

































