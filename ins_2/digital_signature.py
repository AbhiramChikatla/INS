from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

private_key = dsa.generate_private_key(key_size=2048)

public_key = private_key.public_key()

message = b'This is a confidential and important CBIT message.'

signature = private_key.sign(message, hashes.SHA256())

print("Signature:", signature.hex())

try:
    public_key.verify(signature, message, hashes.SHA256())
    print("The Signature is valid.")
except InvalidSignature:
    print("The Signature is invalid.")


"""
Digital signature is a way of authenticating a digital data coming from a trusted source. Digital Signature
Standard (DSS) is a Federal Information Processing Standard(FIPS) which defines algorithms that are used to
generate digital signatures with the help of Secure Hash Algorithm(SHA) for the authentication of electronic
documents. DSS only provides us with the digital signature function and not with any encryption or key
exchanging strategies.
Algorithm for DSA Signature Generation and Verification:
Step 1: Key Generation
• Generate a private key using dsa.generate_private_key(key_size=2048).
• Extract the corresponding public key from the private key.
Step 2: Signing the Message
• Prepare the message that needs to be signed (in this case, b'This is a confidential’).
• Use the private key to sign the message with a specified hash algorithm (SHA-256).
• Obtain the digital signature.
Step 3: Signature Transmission
• The message along with the generated signature can now be transmitted or stored.
Step 4: Signature Verification
• Use public key to verify the signature against the original message and the hash algo.
• If the signature is valid, it confirms the authenticity and integrity of the message.
• If invalid, it indicates tampering or forgery.

Conclusion
The private key signs the message, creating a signature unique to both the message and the signer. The public
key then verifies this signature, ensuring that the message has not been altered and originates from the
legitimate signer. Successful verification confirms trustworthiness, making DSA an essential cryptographic
tool in secure communications."""