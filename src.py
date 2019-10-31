import socket
import random
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",8757))
#frames will be received in list
l=[]

#no of frames that will be received
length=s.recv(10)
lengthint=int(length)

#receive frame one by one
for i in range(0,lengthint):
 data=s.recv(20)
 l.insert(i,data)
for i in l:
 print(i)
 
#generate random no of frame that will resend by server again
randomno=(random.randrange(0,lengthint,1))
print(randomno)
randomno=randomno-1
l[randomno]=-1
print("Received frames are as follow")
for i in l:
 print(i)
randomnostr=str(randomno)
s.send(randomnostr)

#frame that is requested for resend is received:
resent=s.recv(10)
resenint=int(resent)
print("received again")
print(resenint)
s.close()
