from socket import socket
s=socket()
s.bind(("localhost",1238))
s.listen(1)
c,addr=s.accept()
while True:
        msg=raw_input()
        c.send(msg)
        data=c.recv(50)
        print(data)
s.close()
