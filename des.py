from pyDes import des, ECB, PAD_PKCS5
import binascii

key = b"keyibyte"

cipher = des(key, ECB, pad=None, padmode=PAD_PKCS5)

data = "Hello, Data Encryption Standard"

# Encrypt
encrypted_data = cipher.encrypt(data)
print("Encrypted:", binascii.hexlify(encrypted_data))

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data)
print("Decrypted:", decrypted_data.decode())





# Description:
# • DES is a symmetric block cipher developed by IBM in the 1970s and adopted as a
# U.S. federal standard.
# • It operates on 64-bit blocks of plaintext using a 56-bit key (plus 8 parity bits).
# • The algorithm involves:
# 1. Initial Permutation (IP) of input bits.
# 2. 16 rounds of Feistel structure: each round includes expansion, key mixing,
# substitution using S-boxes, and permutation.
# 3. Final Permutation (FP) (inverse of IP).
# • Encryption and decryption follow the same steps, except subkeys are applied in
# reverse order during decryption.
# • Due to its short key length (56 bits), DES is vulnerable to brute-force attacks and is
# now considered insecure for modern applications



# Data Encryption Standard (DES) is a symmetric block cipher. By 'symmetric', we mean that the size of input text and output text (ciphertext) is same (64-bits). The 'block' here means that it takes group of bits together as input instead of encrypting the text bit by bit. Data encryption standard (DES) has been found vulnerable to very powerful attacks and therefore, it was replaced by Advanced Encryption Standard (AES).

# It is a block cipher that encrypts data in 64 bit blocks.
# It takes a 64-bit plaintext input and generates a corresponding 64-bit ciphertext output.
# The main key length is 64-bit which is transformed into 56-bits by skipping every 8th bit in the key.
# It encrypts the text in 16 rounds where each round uses 48-bit subkey.
# This 48-bit subkey is generated from the 56-bit effective key.
# The same algorithm and key are used for both encryption and decryption with minor changes.
# Working of Data Encryption Standard (DES)
# DES is based on the two attributes of Feistel cipher i.e. Substitution (also called confusion) and Transposition (also called diffusion). DES consists of 16 steps, each of which is called a round. Each round performs the steps of substitution and transposition along with other operations.


# Conclusion
# DES was one of the most widely used symmetric key algorithms and introduced important
# concepts like Feistel networks and S-boxes. However, due to its limited key size, it has been
# replaced by stronger algorithms such as Triple DES (3DES) and AES.