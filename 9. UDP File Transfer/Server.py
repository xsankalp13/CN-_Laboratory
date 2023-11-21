import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8080

server_socket.bind((host,port))

output = 'Output.mp3'

with open(output,'wb') as file:
    while True:
        chunk,addr = server_socket.recvfrom(1024)
        print(f'receiving Data:  {chunk}')
        if not chunk:
            break
        file.write(chunk)

print("Transfer done!!")