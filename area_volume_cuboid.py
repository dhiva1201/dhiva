x,y,z=input().split()
L=int(x)
B=int(y)
H=int(z)
TS=2*(L*B + B*H +L*H)
V=L*B*H
print(TS,V)
