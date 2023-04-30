import socket

def calculate_checksum(data):
    # initialize checksum to zero
    checksum = 0
    
    # iterate over each 16-bit word in data and add to checksum
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
    
    # complement and truncate checksum to 16 bits
    checksum = ~checksum & 0xffff
    return checksum

# create a socket object
client_socket = socket.socket()

# get local machine name
host = socket.gethostname()

# connect to the server on a well-known port
client_socket.connect((host, 8088))

while True:
    # receive data and checksum from server
    data = client_socket.recv(1024)
    received_checksum = int.from_bytes(data[-2:], byteorder='big')
    data = data[:-2]
    
    # show the data received from server
    print("Received data:", data)
    
    # calculate checksum of received data
    checksum = calculate_checksum(data)
    
    # check if checksums match
    if checksum == received_checksum:
        # send acknowledgement to server
        client_socket.sendall(b"ACK")
        print("Data received successfully")
    else:
        print("Error detected in data")
        
# close the connection
client_socket.close()
































# import socket

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
# client_socket = socket.socket()

# # get local machine name
# host = socket.gethostname()

# # connect to the server on a well-known port
# client_socket.connect((host, 8080))

# while True:
#     # receive data and checksum from server
#     data = client_socket.recv(1024)
#     received_checksum = int.from_bytes(data[-2:], byteorder='big')
#     data = data[:-2]
    
#     # calculate checksum of received data
#     checksum = calculate_checksum(data)
    
#     # check if checksums match
#     if checksum == received_checksum:
#         # send acknowledgement to server
#         client_socket.sendall(b"ACK")
#         print("Data received successfully")
#     else:
#         print("Error detected in data")
        
# # close the connection
# client_socket.close()
