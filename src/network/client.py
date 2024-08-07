import socket
from data.configs import Configs
configs = Configs()

HEADER = 4096
PORT = 5060
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))
    
send(f"BFDOBFUDOABFDOASBFO-{SERVER}")

while True:
    msg = input()
    if msg == "dc":
        send(DISCONNECT_MESSAGE)
        break
    else:
        send(msg)
    
