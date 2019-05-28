x=int(input())
y=input().split()
for i in range (x):
    if(int(y[i])+1==int(y[i+1])):
        continue
    else:
        break
print(i+1)
