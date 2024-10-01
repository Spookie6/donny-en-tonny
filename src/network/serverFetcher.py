import socket, threading, time, sys, json

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)
sys.path.append(path)

from data.constants import constants

HEADER = constants["SERVER_HEADER"]
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = constants["ENCODING_FORMAT"]
PORT = constants["SERVER_PORT"]

responses = []
times = []

def send(client, msg) -> None:
		message = msg.encode(FORMAT)
		msg_length = len(message)
		send_length = str(msg_length).encode(FORMAT)
		send_length += b' ' * (HEADER - len(send_length))
		client.send(send_length)
		client.send(message)
		package = (json.loads(client.recv(HEADER).decode(FORMAT).split("/")[1]))
		index = package["ip"].split(".")[-1]
		package["ping"] = time.time() * 1000 - times[int(index)]
		responses.append(package)

def ping(ip) -> None:
	remoteServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	remoteServerAddr = (ip, PORT)
	try:
		remoteServer.connect(remoteServerAddr)
		send(remoteServer, constants["SERVER_PINGING_MSG"])
		remoteServer.shutdown(socket.SHUT_RDWR)
		remoteServer.close()
	except:
		pass

def fetchServers(serverList) -> list:
	ipTemplate = ".".join(SERVER.split(".")[:-1])

	for i in range (255):
		try:
			times.append(time.time() * 1000)
			ip = f"{ipTemplate}.{i}"
			thread = threading.Thread(target=ping, args=(ip, ))
			thread.start()
		except:
			pass

	time.sleep(2)
	for item in responses:
		serverList.append(item)

if __name__ == "__main__":
	servers = fetchServers()
	print(servers)