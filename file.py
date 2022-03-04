a=open("demo2","r")
b=open("t.txt","w")
c=a.readlines()
print(c)
d=len(c)
for i in range(0,d):
    if(i%2!=0):
        b.write(c[i])
    else:
        pass
b.close()
b=open("t.txt","r")
e=b.readlines()
print(e)