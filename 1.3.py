x=int(input())
f=[]
while x>0:
    f2=0
    f0,f1=1,1
    i=0
    while f2<=x:
        f0,f1=f1,f1+f0
        f2=f1
        i+=1
    f.append(i)
    x-=f0
print (f)
a=0
for i in range (0,len(f)):
    a+=10**(f[i]-1)
print(a)
