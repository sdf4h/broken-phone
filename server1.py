import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('',8989))
soc.listen(1)
con, addr = soc.accept()
filename = 'qqq.txt'
with open(filename,'wb') as file:
    while True:
        recvfile = con.recv(4096)
        if not recvfile: break
        file.write(recvfile)
print("File has been received.")