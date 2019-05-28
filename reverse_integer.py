x=int(input())
x=str(x)
s=""
c=len(x)-1
for i in range(c,-1,-1):
    s=s+x[i]
print(s)
