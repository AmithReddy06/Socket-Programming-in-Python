import socket
host = socket.gethostname()
port = 6032
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', port))
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
    if message=="Bye" or message=="tata":
        break

print("Closing connection...")
clientsocket.close()
serversocket.close()
