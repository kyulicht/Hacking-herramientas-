import socket

HOST = '0.0.0.0'
PORTS = range(1, 601)

def log_connection(conn, addr):
    print(f'Connection from {addr[0]}:{addr[1]}')
    data = b''
    while True:
        try:
            data += conn.recv(4096)
        except socket.timeout:
            pass
        except socket.error:
            break
    print(f'{len(data)} bytes received')
    conn.close()

for port in PORTS:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, port))
        s.listen()
        print(f'Listening on port {port}...')
        while True:
            conn, addr = s.accept()
            log_connection(conn, addr)