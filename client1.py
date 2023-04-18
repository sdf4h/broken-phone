import socket
soc = socket.socket()
soc.connect(('127.0.0.1',8989))
filename = 'qqq.txt'
with open(filename, 'rb') as file:
    sendfile = file.read()
    soc.sendall(sendfile)
    print('file sent')