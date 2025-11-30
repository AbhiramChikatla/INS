def rail_fence_encrypt(text, key):
    rail = ['' for _ in range(key)]
    row, step = 0, 1

    for ch in text:
        rail[row] += ch
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return "".join(rail)

def rail_fence_decrypt(cipher, key):
    rail_len = [0] * key
    row, step = 0, 1
    for _ in cipher:
        rail_len[row] += 1
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    rails = []
    idx = 0
    for l in rail_len:
        rails.append(list(cipher[idx:idx+l]))
        idx += l

    result = []
    row, step = 0, 1
    for _ in cipher:
        result.append(rails[row].pop(0))
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return "".join(result)

# Example
msg = "HELLOPLUTO"
enc = rail_fence_encrypt(msg, 2)
dec = rail_fence_decrypt(enc, 2)
print("encrypted ->", enc)
print("decrypted ->",dec)



# The Rail Fence Cipher is a simple transposition cipher where the plaintext is written
# diagonally across a number of "rails" (rows), then read row by row.
# • Example with 3 rails for plaintext "HELLO WORLD":
# • Ciphertext is read row by row: HLOLELWRDLO.
# • Decryption reconstructs the zig-zag pattern and retrieves the plaintext.
# • No substitution occurs—only rearrangement of characters.




# Conclusion:
# Rail Fence Cipher demonstrates the concept of transposition by changing the position of
# letters instead of replacing them. It is easy to implement but insecure due to predictable
# pattern