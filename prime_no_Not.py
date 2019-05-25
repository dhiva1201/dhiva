x=int(input())
s=1
for i in range (2,x):
    if((x%i)==0):
        s=0
        break
    else:
        continue
if(s==0):
    print("no")
else:
    print("yes")
