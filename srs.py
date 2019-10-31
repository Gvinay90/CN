#sendind data should be in string or buffer only
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",8757))
s.listen(2)
c,addr=s.accept()
#frames are in list:
l=[10,20,30,40,50]

#no of frames
length=len(l)

#send no of frames 
c.send(str(length))

#send frames one by one:
for i in l:
 print(i)
 c.send(str(i))
 
#frame that need to be resesnd as per request of client
resend=c.recv(10);
resendint=int(resend)

#resend it
c.send(str(l[resendint]))
c.close()



