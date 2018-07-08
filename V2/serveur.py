import socket
import select
from roboc import choose_map, rules
from classes import Robot

host = ''
port = 12800

carte_choisie, carte_en_cours = choose_map()



public_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #builds the listening socket on the server
public_socket.bind((host, port)) #links the socket to the port
public_socket.listen(5) #listens to max 5 clients at a time
print("\nServer is now listening on port {}".format(port))

server_is_listening = True
timeout = 1
connected_sockets = [] #empty for now



while server_is_listening:
    # listening on the public_socket to see if new sockets ask for a connexion
    pending_connection, wlist, xlist = select.select([public_socket], [], [], timeout) #pending connection contains only one socket, the public socket

    #ON ACCEPTE OU REJETTE LA DEMANDE DE CONNEXION
    for socket in pending_connection:
        pending_connection.remove(socket)
        if len(connected_sockets) < 5:
            private_socket, connection_details = socket.accept() #program is blocked until a client asks to connect
            connected_sockets.append(private_socket)
            msg_rules = rules.encode()
            private_socket.send(msg_rules)
            robot_number = str(connected_sockets.index(private_socket)+1)
            msg_robot_number = "\nTon robot sera symbolisé par le chiffre {}".format(robot_number)
            encoded_msg_robot_number = msg_robot_number.encode()
            private_socket.send(encoded_msg_robot_number)

            robot = Robot(robot_number, carte_en_cours) #on crée une instance de Robot à chaque joueur
        else:
            rejected_socket, connection_details = socket.accept()
            msg_full = "\nThe game is full, please try again later".encode()
            rejected_socket.send(msg_full)
            rejected_socket.close()

    sockets_to_read = []
    sockets_to_write_to = []
    xlist = []
    if len(connected_sockets):
        try:
            # LISTENING ON ALL THE PRIVATE SOCKETS
            sockets_to_read, sockets_to_write_to, xlist = select.select(connected_sockets, connected_sockets, connected_sockets, timeout)
        except select.error as error:
            print(error)
            pass
        else:
            # for socket in sockets_to_write_to

            for socket in sockets_to_read:
                msg_received = socket.recv(1024)
                msg_received = msg_received.decode()
                print(socket)  # client's IP and client's port
                print("Reçu : {}".format(msg_received))
                socket.send(b"5/5")
                if msg_received == "end":
                    server_is_listening = False



    

print("\nClosing the connection")
for socket in connected_sockets:
    socket.close()

public_socket.close()