import socket
from _thread import *

serversocket = socket.socket()

host = "127.0.0.1"
port = 9000

ThreadCount = 0

serversocket.bind((host, port))
serversocket.listen(5)

print("Waiting for connection...")

def client_thread(connection):
    connection.send(str.encode("Welcome to the Server!"))
    while True:
        data = connection.recv(2048)
        reply = "Hello I am the server " + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    client, address = serversocket.accept()
    print("Connected to ", address[0] + ":" + str(address[1]))
    start_new_thread(client_thread, (client,))
    ThreadCount += 1
    print("ThreadNumber:", str(ThreadCount))

serversocket.close()



















# import socket
# from _thread import *

# serversocket=socket.socket()

# host="127.0.0.1"
# port=3000

# ThreadCount=0

# try:
#     serversocket.connect((host,port))
# except socket.error as e:
#     print(e)

# print("Waiting for connection...")
# serversocket.listen(5)

# def client_thread(connection):
#     connection.send(str.encode("Welcome to the Server!"))
#     while True:
#         data=connection.recv(2048)
#         reply="Hello I am the server"+data.decode('utf-8')
#         if not data:
#             break
#         connection.sendall(str.encode(reply))
#     connection.close()


# while True:
#     client,address=serversocket.accept()
#     print("Connected to ",address[0]+":"+str(address[1]))
#     start_new_thread(client_thread,(client,))
#     ThreadCount+=1
#     print("ThreadNumber:",str(ThreadCount))
# serversocket.close()