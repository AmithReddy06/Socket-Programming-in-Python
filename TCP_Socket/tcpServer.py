import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',4001)) # 0<port_number<2^16
server_socket.listen(5) # only 5 client sockets can be connected

while True:
    print("Server waiting for connection:")
    client_socket,address = server_socket.accept()
    print("Client connected from",address)
    while True:
        data=client_socket.recv(1024) 
        if not data or data.decode('utf-8')=='END':
            break
        print("Received from client:",data.decode("utf-8"))
        try:
            client_socket.send(bytes('Hey client!','utf-8'))
        except:
            print("Exited by user.")
    client_socket.close()  
server_socket.close()

