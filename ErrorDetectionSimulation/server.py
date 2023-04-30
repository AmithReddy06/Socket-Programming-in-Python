import socket
import random

def calculate_checksum(data):
    """
    Calculate the 16-bit checksum of the given data using the Internet checksum algorithm.
    """
    checksum = 0
    for i in range(0, len(data), 2):
        if i+1 < len(data):
            # combine two bytes into a 16-bit word and add to checksum
            word = (data[i] << 8) + data[i+1]
            checksum += word
        else:
            # if odd number of bytes, pad with zero
            checksum += data[i]
    # add carry to checksum
    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum += (checksum >> 16)
    # complement checksum
    checksum = ~checksum & 0xffff
    return checksum

# create a socket object
server_socket = socket.socket()

# get local machine name
host = socket.gethostname()

# bind the socket to a public host, and a well-known port
server_socket.bind((host, 8088))

# configure the server to listen for incoming connections
server_socket.listen(1)

# accept a connection
conn, addr = server_socket.accept()
print("Connected by", addr)

while True:
    # generate some random data to send
    data = bytes([random.randint(0, 255) for _ in range(10)])
    
    # show the data that is about to be sent
    print("Sending data:", data)
    
    # calculate checksum
    checksum = calculate_checksum(data)
    
    # introduce an error by changing a random byte in the data
    index = random.randint(0, len(data) - 1)
    error_byte = random.randint(0, 255)
    error_data = data[:index] + bytes([error_byte]) + data[index+1:]
    
    # show the data after the error is introduced
    print("Data with error:", error_data)
    
    # send the error data and checksum to client
    conn.sendall(error_data + checksum.to_bytes(2, byteorder='big'))

    # wait for acknowledgement from client
    ack = conn.recv(1024)
    
    # check if acknowledgement is correct
    if ack == b"ACK":
        print("Data sent successfully")
    else:
        print("Error detected in data")
        
# close the connection
conn.close()































# import socket
# import random

# def calculate_checksum(data):
#     checksum = 0
#     for i in range(0, len(data), 2):
#         if i+1 < len(data):
#             # combine two bytes into a 16-bit word and add to checksum
#             word = (data[i] << 8) + data[i+1]
#             checksum += word
#         else:
#             # if odd number of bytes, pad with zero
#             checksum += data[i]
#     # add carry to checksum
#     checksum = (checksum >> 16) + (checksum & 0xffff)
#     checksum += (checksum >> 16)
#     # complement checksum
#     checksum = ~checksum & 0xffff
#     return checksum

# # create a socket object
# server_socket = socket.socket()

# # get local machine name
# host = socket.gethostname()

# # bind the socket to a public host, and a well-known port
# server_socket.bind((host, 8080))

# # configure the server to listen for incoming connections
# server_socket.listen(1)

# # accept a connection
# conn, addr = server_socket.accept()
# print("Connected by", addr)

# while True:
#     # generate some random data to send
#     data = bytes([random.randint(0, 255) for _ in range(10)])
    
#     # calculate checksum
#     checksum = calculate_checksum(data)
    
#     # add error to data
#     data = data[:5] + bytes([random.randint(0, 255)]) + data[6:]
    
#     # send data and checksum to client
#     conn.sendall(data + checksum.to_bytes(2, byteorder='big'))

#     # wait for acknowledgement from client
#     ack = conn.recv(1024)
    
#     # check if acknowledgement is correct
#     if ack == b"ACK":
#         print("Data sent successfully")
#     else:
#         print("Error detected in data")
        
# # close the connection
# conn.close()
