N,A,D=input().split()
N=int(N)
A=int(A)
D=int(D)
s= 0
i = 0
while (i<N): 
  s= s + A 
  A = A+D
  i+=1
print(s)
