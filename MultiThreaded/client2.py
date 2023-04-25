import socket

clientsocket=socket.socket()

host='127.0.0.1'
port=9000

print("Waiting for connection")
try:
    clientsocket.connect((host,port))
except socket.error as e:
    print(str(e))


response=clientsocket.recv(1024)
print(response.decode('utf-8'))

while True:
    inp=input("Say something:")
    clientsocket.send(str.encode(inp))
    response=clientsocket.recv(1024)
    print(response.decode('utf-8'))

clientsocket.close()   