import socket

host = socket.gethostname()
port = 2000

ClientSocket = socket.socket()
print('** Ready to connect **')

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    username = input("Enter username:\t")
    ClientSocket.send(str.encode(username))
    Response = ClientSocket.recv(2048)
    if Response.decode('utf-8') != 'Username is taken':
        break
    print(Response.decode('utf-8'))

print(Response.decode('utf-8'))
while True:
    Input = input('Operation: ')
    if Input == 'BYE':
        ClientSocket.send(str.encode(Input))
        break
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
ClientSocket.close()
