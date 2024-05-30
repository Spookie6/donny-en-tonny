import socket, threading, time, sys

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

class Server:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.server = None
    def handleClient(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg != f"({self.name}, {self.password})":
                    conn.send("Access denied - Incorrect password".encode(FORMAT))
                    connected = False
                    print("Incorrect password")
                    print(f"[{addr}] Disconnected.")
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print(f"[{addr}] Disconnected.")
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
            print(f"[ACTIVE CONNTECTIONS] {threading.active_count() - 1}")
    
    def stop(self):
        print(f"[SERVER]: Shutting down...")
        self.server.shutdown(socket.SHUT_RDWR)
        # self.server.close()
    
    
            
if __name__ == "__main__":
    server = Server("Enrico", "Password")
    thread = threading.Thread(target=server.start)
    thread.start()
    time.sleep(3)
    server.stop()
    sys.exit()