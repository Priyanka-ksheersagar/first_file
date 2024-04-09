import socket
import threading

# You need a server which can first listen with address and port
server_address = socket.gethostbyname(socket.gethostname())
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50000

# Once you have the IP, socket, and port, you would need to bind it to the socket address
socket_address = (server_address, port)
server_socket.bind(socket_address)
clients = []
nicknames = []


def broadcast(brd_msg):
    for client in clients:
        client.send(brd_msg.encode("ascii"))


# once you bind it then you would need to listen to the TCP sessions coming from the client
def handle_client(client):
    try:
        while True:
            client_msg = client.recv(1024).decode("ascii")
            broadcast(client_msg)
    except:
        client_index = clients.index(client)
        clients.remove(client_index)
        nickname = nicknames[client_index]
        broadcast(f"{nickname} has left the chat!!!")
        nicknames.remove(nickname)
        client.close()


def first_func():
    while True:
        server_socket.listen()
        # accepts the connection for client socket and address
        client_socket, client_ip = server_socket.accept()
        print(f"[SERVER ACCEPTED THE CONNECTION FROM {client_ip}]")
        # Now we need to create a separate thread for the connection to handle it in a different function
        # lets create a function which will handle each  client's connection separately

        client_socket.send("NICK".encode("ascii"))

        nickname = client_socket.recv(1024).decode("ascii")
        print(F"{nickname} CONNECTED WITH THE SERVER")

        nicknames.append(nickname)
        clients.append(client_socket)

        broadcast(f"{nickname} joined the chat!!!")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


print("[SERVER STARTING...]")
first_func()
