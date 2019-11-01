import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 10000))

msg, (ip, port) = sock.recvfrom(100)
print "client connected to ip: " + ip + " and port: " + str(port)
print "received message: " + msg
sock.sendto("Hello from server", (ip,port))



while True:    	
	msg, (ip, port) = sock.recvfrom(100)
	print "client connected to ip: " + ip + " and port: " + str(port)
	if "stop." in msg:
		break
	else:			
		print "client: " + msg
	
	msg = raw_input("you: ")
	sock.sendto(msg, (ip,port))
	if "stop." in msg:
		break
sock.close()
#bh@saurabh-HP-Laptop-15g-dr0xxx:~$ python ppudpserv.py
#client connected to ip: 127.0.0.1 and port: 38720
#received message: Hi from client
#client connected to ip: 127.0.0.1 and port: 38720
#client: happy day bro
#you: happy day
#stopclient connected to ip: 127.0.0.1 and port: 38720
#saurabh@saurabh-HP-Laptop-15g-dr0xxx:~$


