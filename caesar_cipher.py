def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(cipher, key):
    return caesar_encrypt(cipher, -key)

# Example
if __name__ == "__main__":
    text = "TESTING"
    key = 3
    enc = caesar_encrypt(text, key)
    dec = caesar_decrypt(enc, key)
    print("Original:", text)
    print("Encrypted:", enc)
    print("Decrypted:", dec)






# Description:


# Ceasar Cipher works by shifting each letter in the plaintext by a fixed number of
# positions in the alphabet.
# • Example: With a shift of 3, A → D, B → E, C → F, etc.
# • Encryption formula:
# C=(P+k)mod  26C = (P + k) \mod 26C=(P+k)mod26
# • Decryption formula:
# P=(C−k)mod  26P = (C - k) \mod 26P=(C−k)mod26
# where PPP is plaintext, CCC is ciphertext, and kkk is the key (shift value).
# • It is easy to implement but insecure, as it can be broken by brute force or frequency
# analysis.




# Conclusion:
# Caesar Cipher introduces the basic idea of substitution techniques and demonstrates how
# encryption can be achieved using a simple shift. However, due to its small key space and
# predictable structure, it is not suitable for modern cryptographic applications.