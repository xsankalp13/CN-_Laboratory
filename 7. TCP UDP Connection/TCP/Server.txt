# Socket Programming using C/C++/Java.
# a. TCP Client, TCP Server


import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

server_socket.bind((host, port))

server_socket.listen(5)
print(f'Server is listing on {host} : {port}.')

client_socket, addr = server_socket.accept()
print(f"Connection has been Established to {addr[0]}")
