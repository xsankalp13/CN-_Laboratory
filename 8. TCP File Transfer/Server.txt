import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

server_socket.bind((host, port))

server_socket.listen(5)
print(f'Server is listing on {host} : {port}.')

client_socket, addr = server_socket.accept()
print(f"Connection has been Established to {addr[0]}")

outputfile = 'OutputFile.txt'

with open(outputfile,'wb') as file:
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        file.write(chunk)

print("Work Done!!")

