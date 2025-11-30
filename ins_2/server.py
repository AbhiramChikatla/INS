
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

context.load_cert_chain(certfile='server_cert.pem', keyfile='server_key.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f'Server listening on {HOST}:{PORT}...')

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f'Connection from {addr}')

        data = conn.recv(1024)
        print(f'Received: {data.decode()}')

        conn.sendall(b'Hello from SSL server!')

        conn.close()
