import socket
import threading

HEADER = 64
PORT = 9999
KNOWN_PORT = 5555
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket for client
client.connect(ADDR) #connects client socket to server

ip = client.recv(2048).decode(FORMAT) #Recieve peer's ip from tracker server
dest_port = client.recv(2048).decode(FORMAT) # Recieve peer's port number from tracker server
dest_port = int(dest_port) #Convert port back to int
src_port = KNOWN_PORT

#Print peer's information
print("[PEER CONNECTED]")
print(f"IP:               {ip}")
print(f"Source Port:      {src_port}")
print(f"Dest Port:        {dest_port}")

#UDP hole punching
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
sock.bind((ip, src_port))
sock.sendto(b'0', (ip, dest_port))

print('ready to exchange messages\n')

# listen for incoming connections
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
    sock.bind((ip , src_port))

    while True:
        data = sock.recv(1024)
        print(f'\rpeer: {data.decode(FORMAT)}\n> ', end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

# send data
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
sock.bind((ip, dest_port))

while True:
    msg = "53.3438° N, 6.2546° W"
    input()
    sock.sendto(msg.encode(FORMAT), (ip, src_port))