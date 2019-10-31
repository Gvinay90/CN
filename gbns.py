from socket import socket
import time
s=socket()
s.bind(("localhost",2002))
s.listen(1)
c,addr=s.accept()
no=int(c.recv(100).decode())
mode=int(c.recv(100).decode())
f={}
for i in range(no):
        f[i]=False
if(mode==1):
        for i in range(no):
                print("Sending frame no " + str(i))
                data=str(i).encode()
                c.send(data)
                print("waiting for ack")
                time.sleep(5)     
                data=c.recv(100)
                print("Received ack for frame no "+ str(i) +" as "+data.decode())
else:   
        for i in range(no):
                if(i==2):
                        print("Sending frame no " +str(i))
                else:
                        print("Sending frame no" + str(i))
                        c.send(str(i).encode())
                        print("Waiting for ack ")
                        time.sleep(5)
                        data=c.recv(100)
                        if(data.decode()!="-1"):   
                                f[i]=True
                                print("Received ack for frame no "+ str(i) +"as"+data.decode())
                            
        for i in f.keys():
                if(f[i]==False):
                        print("Resending frame no" + str(i))
                        c.send(str(i).encode())
                        print("Waiting for ack ")
                        time.sleep(5)
                        data=c.recv(100)
                        print("Received ack for frame no "+ str(i) +"as"+data.decode())   
                        f[i]=True
                                                 
s.close()
