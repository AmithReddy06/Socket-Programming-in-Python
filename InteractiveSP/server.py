import socket
host = socket.gethostname()
port = 6030
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', port))
serversocket.listen(1)
print("Waiting for a client connection...")
clientsocket, address = serversocket.accept()
print("Connected to client:", address)
while True:
    message = clientsocket.recv(1024).decode()
    if not message:
        break
    print("Client:", message)
    if message=="Bye":
        break
    response = input("Server: ")
    clientsocket.send(response.encode())
    if message=="Bye":
        break

print("Closing connection...")
clientsocket.close()
serversocket.close()
