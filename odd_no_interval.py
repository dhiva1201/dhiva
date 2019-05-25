x=input()
x=x.split()
a=int(x[0])
b=int(x[1])
s=""
for i in range (a+1,b):
    if((i%2)!=0):
        s=s+str(i)+" "
    else:
        continue
print(s)
