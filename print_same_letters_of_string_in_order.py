n=input()
n=int(n)#4
l=[]
for i in range(0,s):  #dhivakar dhivagar emaya durga
    s1=input()
    l.append(s1)
Z=[]
for i in zip(*l): #i=('d', 'd', 'e', 'd')
    if i.count(i[0])==len(i): #3==4
        Z.append(i[0])
    else:
        break
print(''.join(Z))
