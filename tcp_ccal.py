from socket import socket
c=socket()
c.connect(("localhost",2004))
exp=input("Enter the expression").encode()
c.send(exp)
print(c.recv(50).decode())

