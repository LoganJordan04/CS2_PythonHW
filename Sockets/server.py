import socket

# Define the host to the IP of the system the script is executed on.
HOST = socket.gethostbyname(socket.gethostname())
# Define the port of the server.
PORT = 9090

# Create a new socket and bind it to the address.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Enable the server to accept connections.
server.listen(5)

# Infinite loop to keep the server running until manually stopped.
while True:
    # Accept a connection. The socket must be bound to an address and listening for connections.
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    # Receive data from the socket, with the maximum amount of data to be received at once is 1024 bytes.
    message = communication_socket.recv(1024).decode("utf-8")
    print(f"Message from client is: {message}")
    # Send data to the socket. The string is converted to bytes using utf-8 encoding
    communication_socket.send(f"Got your message! Thank you!".encode("utf-8"))
    # Mark the socket closed.
    communication_socket.close()
    print(f"Connection with {address} ended!")
