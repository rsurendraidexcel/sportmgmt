import socket
import threading
import time

PORT = 5050
FORMAT = 'utf-8'
HEARDER = 64
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

web_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
web_server.bind(ADDR)

def handle_client(conn, addr):
    print(f'[New Connection] {addr} connected')
    connected = True
    while connected:
        msg_length = conn.recv(HEARDER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f'[{addr}] {msg}')

    conn.close()


def start():
    web_server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}:{PORT}')
    while True:
        conn, addr = web_server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f'[Active Connection ] {threading.active_count() - 1 }') 


print(f'[Starging] Server is start')
start()
