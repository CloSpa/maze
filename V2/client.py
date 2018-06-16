import socket

host = "localhost"
port = 12800

connexion_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #build the bridging socket
connexion_with_server.connect((host, port)) #connects client to server
print("Client connected to server's public socket on port {}".format(port))


msg_received = connexion_with_server.recv(10000)
print(msg_received.decode())




msg_to_send = b""
while msg_to_send != b"end":
    msg_to_send = input("> ")
    msg_to_send = msg_to_send.encode()
    connexion_with_server.send(msg_to_send)
    msg_received = connexion_with_server.recv(1024)
    print(msg_received.decode())

print("Closing the connexion")
connexion_with_server.close()