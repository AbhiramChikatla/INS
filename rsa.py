from math import *

def power(base, expo, m):
    return pow(base,expo,m)

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1


def generateKeys():
    p = 3
    q = 11

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that gcd(e, phi) = 1
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Find d such that (e * d) % phi = 1
    d = modInverse(e, phi)

    return e, d, n

# Encrypt using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)

# Decrypt using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)

# Main
if __name__ == "__main__":
    # Key Generation
    e, d, n = generateKeys()

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message
    M = 31
    print(f"Original Message: {M}")

    # Encryption
    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    # Decryption
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")
