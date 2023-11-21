import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8080



message = "Hello from Client"
client_socket.sendto(message.encode('utf-8'),  (host, port))

print(f'Connection established ')