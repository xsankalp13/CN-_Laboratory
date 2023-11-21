import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8080
inputFile = 'input.mp3'
with open(inputFile, 'rb') as file:

    while True:
        chunk = file.read(1024)
        if not chunk:
            break
        client_socket.sendto(chunk,(host,port))

print("Sent Successfully ")