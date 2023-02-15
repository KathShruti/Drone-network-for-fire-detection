import socket
import threading 

HEADER = 64
PORT = 9999
KNOWN_PORT = 50002
SERVER = socket.gethostbyname(socket.gethostname()) #Gets IP of server
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates new socket
server.bind(ADDR) #binds new socket to ADDR
clients = []
conns = []

#runs when there are two clients checked in with the server, sends clients ip and port number to each other
def handle_client():

    connected = True
    while connected:
        c1 = clients[0]
        c1_addr, c1_port = c1
        c2 = clients[1]
        c2_addr, c2_port = c2
        conn1 = conns[0]
        conn2 = conns[1]

        conn1.send(str(c2_addr).encode(FORMAT))
        conn1.send(str(c2_port).encode(FORMAT))
        conn2.send(str(c1_addr).encode(FORMAT))
        conn2.send(str(c1_port).encode(FORMAT))
    
    conn1.close()
    conn2.close()

#function to allow server to start listening for connections
def start():
    server.listen() #Server listens for new connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #When new connection is made, port and ip is stored in addr and object is stored in conn
        clients.append(addr)
        conns.append(conn)
        print(f"[NEW CONNECTION] {addr} connected.")
        print(f"[ACTIVE CONNECTIONS] {len(clients)}") #Prints 1 active connection when 2 threads are running
        if (len(clients)) == 2:
            thread = threading.Thread(target = handle_client) #Passes conn and addr of new connection to handle_client
            thread.start() #Starts thread

print("[STARTING] tracker server is starting...")
start()