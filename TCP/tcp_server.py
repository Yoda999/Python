import socket
import threading
IP = '0.0.0.0'
PORT = 9998 

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ip,PORT)
    server.listen(5)
    print(f'[*] listening on port {ip} {port}')

while True:
    client,address = server.accept()
    print(f'[*] server accepted connection form {address[0]}:{address[1]}')
    client_handler = threading.Thread(target = handle_client, args = client)
    client_handler.start()
    
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(B'ACK')

if __name__ == '__main__':
    main()
    
    

