import socket
from sys import stdin, stdout
from select import select

host = "localhost"
port = 12800
BUFFER_SIZE = 4096
SELECT_TIMEOUT = 5
msg_received = ""

connexion_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #build the bridging socket
connexion_with_server.connect((host, port)) #connects client to server
print("Client connected to server's public socket on port {}".format(port))

streamsToWatch = [connexion_with_server] # We will watch for read/writes on the socket w/ the server

while msg_received != "\nThe game is full, please try again later":
    readList, writeList, errorList = select(streamsToWatch, streamsToWatch, streamsToWatch, SELECT_TIMEOUT)
    for stream in readList:
        msg_received = stream.recv(BUFFER_SIZE).decode()
        print(msg_received)
    if msg_received is "\nA toi d'jouer !":
        buffer = input() # stdin clavier
        connexion_with_server.send(buffer.encode())
    if len(errorList) is not 0:
        exit(-1)


print("\nClosing the connexion")
connexion_with_server.close()