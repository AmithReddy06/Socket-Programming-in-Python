import socket

# Create socket with socket class.
master = socket.socket()

# Host is the IP address of master
# machine.
host = "192.168.93.149"

# This will be the port that the
# socket is bind.
port = 8088

# binding the host and port to the
# socket we created.
master.bind((host, port))

# listen method listens on the socket
# to accept socket connection.
master.listen(1)

# This method accept socket connection
# from the slave machine
slave, address = master.accept()

# When the slave is accepted, we can send
# and receive data in real time
while True:
	# input the command from the user
	print(">", end=" ")
	command = input()

	# encode the command and send it to the
	# slave machine then slave machine can
	# executes the command
	slave.send(command.encode())

	# If the command is exit, close the connection
	if command == "exit":
		break

	# Receive the output of command, sent by the
	# slave machine.recv method accepts integer as
	# argument and it denotes no.of bytes to be
	# received from the sender.
	output = slave.recv(5000)
	print(output.decode())

# close method closes the socket connection between
# master and slave.
master.close()
