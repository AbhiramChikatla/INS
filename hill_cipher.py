import numpy as np

key_matrix = np.zeros((3, 3), dtype=int)
message_vector = np.zeros((3, 1), dtype=int)
cipher_matrix = np.zeros((3, 1), dtype=int)

def get_key_matrix(key):
   k = 0
   for i in range(3):
      for j in range(3):
         key_matrix[i][j] = ord(key[k]) % 65
         k += 1

def encrypt(message_vector):
   for i in range(3):
      cipher_matrix[i][0] = 0
      for x in range(3):
         cipher_matrix[i][0] += (key_matrix[i][x] * message_vector[x][0])
      cipher_matrix[i][0] = cipher_matrix[i][0] % 26

def hill_cipher(message, key):
   get_key_matrix(key)
   for i in range(3):
      message_vector[i][0] = ord(message[i]) % 65
   encrypt(message_vector)
   ciphertext = [chr(cipher_matrix[i][0] + 65) for i in range(3)]
   print("The Ciphertext:", "".join(ciphertext))

message = "LION"
key = "NUREKYHGI"
print("message is",message)
hill_cipher(message, key)




# Description:
# • Hill Cipher uses an n×n key matrix (invertible modulo 26).
# • Plaintext is represented as numerical vectors (A=0, B=1, … Z=25).
# • Encryption:
# C=K×P mod  26
# • Decryption requires the inverse of the key matrix:
# P=K^-1×C mod  26.
# • Since it works on blocks (e.g., 2×2 or 3×3 matrices), it hides frequency patterns better
# than monoalphabetic and digraph ciphers.



# Conclusion:
# Hill Cipher demonstrates the use of linear algebra in cryptography and provides a more
# complex and secure encryption method than Caesar or Playfair ciphers. However, it is
# vulnerable to known plaintext attacks and requires careful key selection (invertible matrix).