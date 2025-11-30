import hashlib
my_string = "Hello, Tutorialspoint!"
my_bytes = my_string.encode('utf-8')
hash_object = hashlib.sha256()
hash_object.update(my_bytes)
hash_hex = hash_object.hexdigest()
print("SHA-256 hash of", my_string, ":", hash_hex)


"""
SHA-512, or Secure Hash method 512, is a hashing technique that converts text of arbitrary length into a fixed-size string. Each output has a SHA-512 length of 512 bits (64 bytes).

This algorithm is frequently used for email address hashing, password hashing, and digital record verification. SHA-512 is also used in blockchain technology, with the BitShares network becoming the most known example.
    
    
SHA-512 Logic The algorithm takes as input a message with a maximum length of less than  2^128 bits and produces as output a 512-bit message digest. The input is processed in 1024-bit blocks. 
Step 1 Append padding bits. The message is padded so that its length is congruent to 896 modulo 1024[length=896(mod1024) . Padding is always added, even if the message is already of the desired length. Thus, the number of padding bits is in the range of 1 to 1024. The padding consists of a single 1 bit followed by the necessary number of 0 bits.
Step 2:append length. A block of 128 bits is appended to the message. This block is treated as an unsigned 128-bit integer In Figure 11.8, the expanded message is repre- sented as the sequence of 1024-bit blocks M1,M2,…..𝑀_𝑁, so that the total length of the expanded message is N*1024 bits
Step 4 Process message in 1024-bit (128-word) blocks. The heart of the algorithm
is a module that consists of 80 rounds; this module is labeled F . 
Each round takes as input the 512-bit buffer value, abcdefgh, and updates the contents of the buffer.At input to the first round, the buffer has the value of the intermediate hash value𝐻_(𝑖−1) .
"""