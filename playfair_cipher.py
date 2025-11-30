def playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J","I") + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [list(key[i:i+5]) for i in range(0,25,5)]

def pos(matrix, c):
    for i in range(5):
        if c in matrix[i]:
            return i, matrix[i].index(c)

def prepare(text):
    text = text.upper().replace("J","I")
    res, i = "", 0
    while i < len(text):
        a, b = text[i], text[i+1] if i+1 < len(text) else "X"
        if a == b: res += a+"X"; i += 1
        else: res += a+b; i += 2
    return res

def encrypt(text, key):
    M, text, out = playfair_matrix(key), prepare(text), ""
    for a,b in zip(text[0::2], text[1::2]):
        r1,c1 = pos(M,a); r2,c2 = pos(M,b)
        if r1==r2: out += M[r1][(c1+1)%5]+M[r2][(c2+1)%5]
        elif c1==c2: out += M[(r1+1)%5][c1]+M[(r2+1)%5][c2]
        else: out += M[r1][c2]+M[r2][c1]
    return out

def decrypt(cipher, key):
    M, out = playfair_matrix(key), ""
    for a,b in zip(cipher[0::2], cipher[1::2]):
        r1,c1 = pos(M,a); r2,c2 = pos(M,b)
        if r1==r2: out += M[r1][(c1-1)%5]+M[r2][(c2-1)%5]
        elif c1==c2: out += M[(r1-1)%5][c1]+M[(r2-1)%5][c2]
        else: out += M[r1][c2]+M[r2][c1]
    return out

# Example
if __name__ == "__main__":
    text, key = "ATTACK", "MONARCHY"
    enc = encrypt(text, key)
    dec = decrypt(enc, key)
    print("Original:", text)
    print("Encrypted:", enc)
    print("Decrypted:", dec)



# Description
# A 5×5 matrix is constructed using a keyword (e.g., "MONARCHY"). The remaining
# letters of the alphabet are filled in sequence.
# • Plaintext is divided into pairs (digraphs). If a pair has repeated letters, an extra
# character (commonly X) is inserted.
# • Encryption rules:
# 1. If both letters are in the same row → replace each with the letter to its right.
# 2. If both letters are in the same column → replace each with the letter below it.
# 3. Otherwise, replace with letters at the rectangle’s corners.
# • Decryption follows the reverse rules.



# Conclusion:
# Playfair Cipher improves security over Caesar Cipher by encrypting digraphs, making
# frequency analysis more difficult. Still, it is not fully secure against modern attacks but
# represents a significant historical step in classical cryptography.