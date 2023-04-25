import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind(('127.0.0.1',2000))

while True:
    data,address=sock.recvfrom(4096)
    print(str(data))
    message= "Hello, I am the UDP Server".encode('utf-8')
    sock.sendto(message,address)

    
