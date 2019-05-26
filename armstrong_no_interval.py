x,y = input().split()
a=int(x)
b=int(y)
for i in range(a + 1 , b ):
        i=str(i)
        s=0
        for j in range (0,len(i)):
                s=s+(int(i[j])**3)
        if(int(i)==s):
                        print(s, end=" ")
