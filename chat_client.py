import socket
import threading

nickname = input("Enter the nickname to connect to the server: ")
# You need a server which can first listen with address and port

server_ip = "127.0.0.1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 50000
server_sock = (server_ip,port)
client_socket.connect(server_sock)



def client_send():
    while True:
        try:
            server_msg = client_socket.recv(1024).decode("ascii")
            if server_msg == "NICK":
                client_socket.send(nickname.encode("ascii"))
            else:
                print(server_msg)
        except:
            print("some error occurred closing the connection from the client side")
            client_socket.close()
            break


def write():
    while True:
        client_socket.send(f"{nickname}: {input('')}".encode("ascii"))


client_send_thread = threading.Thread(target=client_send)
client_send_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


