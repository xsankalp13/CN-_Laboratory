# b. UDP Client, UDP Serve
import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8080

server_socket.bind((host, port ))

print(f" server is listing on {host}:{port}")

data, addr = server_socket.recvfrom(1024)
print(f'message from {addr[0]} is saying {data}')