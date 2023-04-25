import socket
import sys

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # should use SOCK_DGRAM for udp
except socket.error as e:
    print("Failed")
    print("Reason:"+str(e))
    sys.exit()

print('Socket Created')    

target_host=input("Enter the target_host name to connect:")
target_port=input("Enter the target_port:")
try:
    sock.connect((target_host,int(target_port)))
    print("Socket Connected To:"+target_host,"on",target_port)
    sock.shutdown(2)
except socket.error as e:
    print("Failed to connect to",target_host,"-",target_port)
    print("Reason:",str(e))
    sys.exit()


