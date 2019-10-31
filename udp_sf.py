import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr=('localhost',2000)
sock.bind(server_addr)
data,address=sock.recvfrom(1000)
print(data.decode())
sock.sendto("Hello".encode(),address)
sock.close()
