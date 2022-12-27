import socket
from _thread import *
import filesystem as fs

host = socket.gethostname()
port = 2000
ThreadCount = 0

usernames = ['ahmad']


def client_handler(connection):

    while True:
        data = connection.recv(2048)
        username = data.decode('utf-8')
        print('Username entered is: ' + username)
        if username not in usernames:
            break
        connection.send(str.encode('Username is taken'))

    usernames.append(username)
    print('\t** ' + username + ' is connected **')
    connection.send(str.encode('\t** ' + username + ' is connected **'))
    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        print(f'{username} --> ')
        fs.thread_function(message)
        if message == 'BYE':
            print('\t** ' + username + ' has disconnected')
            break
        reply = f'{username} --> {message} : SUCCESS'
        connection.sendall(str.encode(reply))
    usernames.remove(username)
    connection.close()


def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to socket ---> ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))


def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'\n\t** Server is listing on the port {port} **')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)


start_server(host, port)
