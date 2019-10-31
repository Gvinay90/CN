input=input("Enter ip address along with cidr")
addrstring,cidrstring=input.split("/")
addr=addrstring.split(".")
cidr=int(cidrstring)
mask=[0,0,0,0]
for i in range(cidr):
        mask[i//8]=mask[i//8]+(1<<(7-i%8))
net=[]
for i in range(4):
        net.append(int(addr[i]) & mask[i])
broad=list(net)
brange=32-cidr
for i in range(brange):
        broad[3-i//8]=broad[3-i//8]+(1<<(i%8))
print(broad)
print(net)
print(mask)
