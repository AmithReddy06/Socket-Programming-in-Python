import socket

# host = 'localhost'
port = 6032
# host = socket.gethostname()
# host = '192.168.1.109'
host='127.0.0.1'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

while True:
    message = input("Client: ")
    clientsocket.send(message.encode())
    response = clientsocket.recv(1024).decode()
    print("Server:", response)
    if response == "Bye" or response=="tata": # original
        break

print("Closing connection...")
clientsocket.close()
