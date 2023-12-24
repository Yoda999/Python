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
    
    

