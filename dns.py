import socket
addr=socket.gethostbyname("yahoo.com")
print(addr)
name=socket.gethostbyaddr(addr)
print(name)
