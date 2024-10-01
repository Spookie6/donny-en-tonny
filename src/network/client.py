import socket, threading
from data.configs import Configs
configs = Configs()
from data.constants import constants

HEADER = 4096
PORT = 5060
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

class Client:
    def __init__(self, remoteIp, ) -> None:
        self.remoteAddr = (remoteIp, constants["SERVER_PORT"])
        self.client = None
        self.thread = None
        self.res = ""
        self.msg = ""
        
    def send(self, msg) -> str:
        if not self.client:
            return Exception("Not connected to a remote server")
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print("in send ", self.client.recv(HEADER).decode(FORMAT))
        return self.client.recv(HEADER).decode(FORMAT)
        
    def connect(self, password):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        def thread():
            self.client.connect(self.remoteAddr)
            last_send = None
            while True:
                print(self.msg != last_send)
                if self.msg != last_send:
                    self.res = self.send(self.msg)

        self.thread = threading.Thread(target=thread,)
        self.thread.start()
        self.msg = password
        
    def disconnect(self):
        self.send(DISCONNECT_MESSAGE)