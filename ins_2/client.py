"""
after entering into Internal2 Folder , use these commands

sudo apt install openssl -y
'''openssl req -newkey rsa:2048 -nodes -keyout server_key.pem -x509 -days 365 -out server_cert.pem \
  -subj "/C=IN/ST=Telangana/L=Hyderabad/O=CBIT/OU=CSE/CN=localhost"'''

"""
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

context = ssl.create_default_context()

context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.sendall(b'Hello from SSL client!')
        data = ssock.recv(1024)
        print(f'Received: {data.decode()}')
