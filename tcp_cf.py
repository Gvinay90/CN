from socket import socket
c=socket()
c.connect(("localhost",2002))
data=c.recv(100)
file=open("output.txt","w")
file.write(data)

