import socket
from data.configs import Configs
configs = Configs()

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

class Client:
    def __init__(self, server_name, server_password):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)

        self.server_credentials = f"({server_name}, {server_password})"
        
    def connect(self):
        self.send(self.server_credentials)
        
    def send(self, msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(HEADER).decode(FORMAT))
        
    # send("(Enrico, Password)")