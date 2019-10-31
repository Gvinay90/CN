from socket import socket
c=socket()
c.connect(("localhost",1238))
while True:
        data=c.recv(50)
        print(data)
        msg=raw_input()
        c.send(msg)
