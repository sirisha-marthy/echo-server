import select 
import socket
import datetime

host = ''
port = 10000

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(5)
inputs = [server]

while True:
    inputready,outputready,exceptready = select.select(inputs, inputs, [], 5)
    if  not inputready:
         print('Server running at {}'.format(datetime.datetime.now()))
    for s in inputready:
        if s is server:
            clientsock, clientaddr = server.accept()
            inputs.append(clientsock)
            print('Client connected from {}', clientaddr)
        else:
            data = s.recv(1024)
            print('{}: {}'.format(s.getpeername(), data))
            if not data:
                s.close()
                inputs.remove(s)
            else:
                s.send(data)


server.close()
                    


