from socket import socket
s=socket()
s.bind(("localhost",2002))
s.listen(1)
c,addr=s.accept()
f=open("input.txt","r")
data=f.read(50)
c.send(data)
c.close()

