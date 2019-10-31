from socket import socket
s=socket()
s.bind(("localhost",2004))
s.listen(1)
c,addr=s.accept()
exp=c.recv(50).decode()
l=exp.split(" ")
res=0
if(l[1]=='+'):
        res=int(l[0])+int(l[2])
elif(l[1]=='-'):
        res=int(l[0])-int(l[2])
elif(l[1]=='*'):
        res=int(l[0])*int(l[2])
else:
        res=int(l[0])/int(l[2])                
c.send(str(res).encode())
