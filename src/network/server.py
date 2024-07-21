import socket, threading, sys, json

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

from data.constants import constants

HEADER = 4096
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def send(client, msg):
		message = msg.encode(FORMAT)
		msg_length = len(message)
		send_length = str(msg_length).encode(FORMAT)
		send_length += b' ' * (HEADER - len(send_length))
		client.send(send_length)
		client.send(message)
  
class Server:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.server = None
        self.connections = []
        self.msg = ""
        self.playerCount = 1
        
    def handleClient(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        print(conn, addr)
        
        connected = True
        last_send = ""
        while connected:
            if last_send != self.msg:
                conn.send(self.msg.encode())
                last_send = self.msg
            
            msg_length = conn.recv(HEADER).decode(FORMAT)
            
            if msg_length:
                msg_length = int(msg_length)
                try:
                    msg = conn.recv(msg_length).decode(FORMAT)
                except:
                    pass
                
                if msg == constants["SERVER_PINGING_MSG"]:
                    package = {
                        "ip": SERVER,
                        "name": self.name,
                        "playerCount": self.playerCount - 1,
                    }
                    
                    json_package = json.dumps(package)
                    message = constants["SERVER_PINGING_MSG"] + "/" + json_package
                    conn.send(message.encode(FORMAT))
                    self.playerCount -= 1
                    connected = False
                    break
                    
                elif msg != f"({self.name}, {self.password})":
                    conn.send("Access denied - Incorrect password".encode(FORMAT))
                    connected = False
                    print("Incorrect password")
                    print(f"[{addr}] Disconnected.")
                    self.playerCount -= 1
                    
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[{addr}] Disconnected.")
                    self.playerCount -= 1
                    break

                print(f"[{addr}] {msg}")
                conn.send("Msg received.".encode(FORMAT))

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        self.server.listen()
        print(f"[LISTENING] Server is listening on {SERVER} - Name: {self.name} - Password: {self.password}")
        
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handleClient, args=(conn, addr))
            thread.start()
            self.playerCount += 1
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
    def stop(self):
        print(f"[SERVER]: Shutting down...")
        self.server.shutdown(socket.SHUT_RDWR)
        
    def send(self, msg):
        self.msg = msg
            
if __name__ == "__main__":
    server = Server("enrico", "arend")
    thread = threading.Thread(target=server.start)
    thread.start()
    
    while True:
        msg = input("MSG: ")
        server.send(msg)