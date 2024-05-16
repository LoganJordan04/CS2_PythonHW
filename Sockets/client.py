import socket

# Define the host to the IP of the system the script is executed on.
HOST = socket.gethostbyname(socket.gethostname())
# Define the port of the client.
PORT = 9090

# Create a new socket and bind it to the address.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

# Send data to the socket. The string is converted to bytes using utf-8 encoding.
socket.send("Hello World!".encode("utf-8"))
# Receive data from the socket, with the maximum amount of data to be received at once is 1024 bytes.
print(socket.recv(1024).decode("utf-8"))
