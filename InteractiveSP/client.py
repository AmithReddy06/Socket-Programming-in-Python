import socket

# host = 'localhost'
port = 6006
# host = socket.gethostname()
host = '192.168.1.109'

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

while True:
    message = input("Client: ")
    clientsocket.send(message.encode())
    response = clientsocket.recv().decode()
    print("Server:", response)
    if response == "Bye": # original
        break

print("Closing connection...")
clientsocket.close()
