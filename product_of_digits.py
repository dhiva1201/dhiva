a=int(input())
product=1
while(a!=0):
    k=a%10
    product=product*k
    a=a//10
print(product)
