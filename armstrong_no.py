x=input()
s=0
for i in range (0,len(x)):
        s=s+(int(x[i])**3)
s=str(s)
if(x==s):
        print("yes")
else:
        print("no")
