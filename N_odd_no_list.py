x=input()
x=x.split()
N=int(x[0])
K=int(x[1])
y=input()
y=y.split()
a=[]
j=1
for i in range (N):
    d=int(y[i])
    if ((d%2)!=0):
        a.append(y[i])
while(j!=K):
    j+=1
print(a[j-1])
