from socket import socket
s=socket()
s.connect(("localhost",2002))
no=input("Enter the number of frames to be received")
s.send(no.encode())
mode=input("Enter the type of transmission 0.Error 1.No Error")
s.send(mode.encode())
check=0
if(mode=="1"):
        for j in range(int(no)):
                print("Received frame number " + str(j))
                print("Sending ack for frame no " + data)
                data=s.recv(100).decode()
                s.send(data.encode())
               
else:
        j=0
        while(j<int(no)-1):
                data=s.recv(100).decode()
                #data=int(data)
                if(int(data)==check):
                        print("Received frame number " + str(data))
                        print("Sending ack for frame no " + str(data))
                        s.send(data.encode())
                        check+=1
                else:
                        j-=j
                        print("Discarded frame no "+ str(data))
                        print("Sending negative ack ")
                        s.send("-1".encode())           
s.close()
