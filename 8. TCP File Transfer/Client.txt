import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

client_socket.connect((host, port))
print("Connection Done")

filename = 'SendingFile'

with open(filename, 'rb') as file:
    while True:
        chunk = file.read(1024)
        if not chunk:
            break
        client_socket.send(chunk)

print("Sent Succesful.")