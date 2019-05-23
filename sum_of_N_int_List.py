x=input()
x=x.split()
N=int(x[0])
K=int(x[1])
y=input()
y=y.split()
s=0
for i in range(K):
    s=s+int(y[i])
print(s)
#given N ,K and N array find sum of first K integer
