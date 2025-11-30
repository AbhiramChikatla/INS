import math

def columnar_encrypt(plaintext, keyword):
    # Prepare the keyword order
    key_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    
    # Calculate grid dimensions
    num_cols = len(keyword)
    num_rows = math.ceil(len(plaintext) / num_cols)
    
    # Pad plaintext if necessary
    padded_plaintext = plaintext.ljust(num_rows * num_cols, '_')
    
    # Create the matrix
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    k = 0
    for r in range(num_rows):
        for c in range(num_cols):
            matrix[r][c] = padded_plaintext[k]
            k += 1
            
    # Read columns in keyword order to form ciphertext
    ciphertext = ""
    for col_index in key_order:
        for r in range(num_rows):
            ciphertext += matrix[r][col_index]
            
    return ciphertext

def columnar_decrypt(ciphertext, keyword):
    # Prepare the keyword order (same as encryption)
    key_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    
    # Calculate grid dimensions
    num_cols = len(keyword)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    
    # Create an empty matrix for decryption
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill the matrix column by column based on keyword order
    char_index = 0
    for col_index in key_order:
        for r in range(num_rows):
            matrix[r][col_index] = ciphertext[char_index]
            char_index += 1
            
    # Read rows to form plaintext
    plaintext = ""
    for r in range(num_rows):
        for c in range(num_cols):
            plaintext += matrix[r][c]
            
    # Remove padding characters
    return plaintext.replace('_', '').strip()

# Example Usage
plaintext = "ZOOLOGY"
keyword = "HACK"

encrypted_text = columnar_encrypt(plaintext, keyword)
print(f"Encrypted: {encrypted_text}")
decrypted_text = columnar_decrypt(encrypted_text, keyword)
print(f"Decrypted: {decrypted_text}")



# Description
# Plaintext is written row by row into a rectangular matrix.
# • A permutation key determines the new order of columns.
# • Example:
# Plaintext = "HELLOWORLD"
# Matrix with 5 columns:
# H E L L O
# W O R L D
# Key = (3,1,5,2,4) → Columns reordered.
# • Ciphertext is obtained by reading the matrix column by column after applying the
# permutation.
# • Decryption requires applying the inverse column permutation to restore the original
# text.



# Conclusion:
# Column Transformation Cipher provides stronger encryption than Rail Fence and Row
# Transformation by scrambling text both horizontally and vertically. However, it can still be
# broken with frequency analysis and is mainly of historical interest.