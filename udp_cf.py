import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=("localhost",2000)
msg="Hello there"
sock.sendto(msg.encode(),server_address)
data,server=sock.recvfrom(1000)
print(data.decode())
sock.close()
