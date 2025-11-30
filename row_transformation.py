def row_trans_encrypt(message, key):
    n = len(key)
    rows = [message[i:i+n] for i in range(0, len(message), n)]
    cipher = []
    for row in rows:
        for idx in key:                 # write chars in key order
            if idx-1 < len(row):        # skip positions not present in short last row
                cipher.append(row[idx-1])
    return "".join(cipher)

def row_trans_decrypt(cipher, key):
    n = len(key)
    L = len(cipher)
    num_rows = (L + n - 1) // n         # ceil(L/n)
    last_len = L % n or n               # length of last row

    pos = 0
    rows = []
    for r in range(num_rows):
        this_len = n if (r < num_rows - 1) else last_len
        row = [''] * this_len
        for idx in key:                 # read in the same key order we wrote
            if idx <= this_len:
                row[idx - 1] = cipher[pos]
                pos += 1
        rows.append("".join(row))
    return "".join(rows)

# Example
msg = "TESTING"
key = [3, 1, 2]
enc = row_trans_encrypt(msg, key)
dec = row_trans_decrypt(enc, key)
print("Encrypted:", enc)  
print("Decrypted:", dec)  



# Description:
# • Plaintext is written row by row into a rectangular matrix.
# • A permutation key determines the new order of rows.
# • Example:
# Plaintext = "HELLOWORLD"
# Matrix (3 rows):
# H E L L
# O W O R
# L D X X
# Key = (3,1,2) → Rows reordered.
# • Ciphertext is obtained by reading row by row after transformation.
# • Decryption requires rearranging rows back to their original order using the inverse of
# the key