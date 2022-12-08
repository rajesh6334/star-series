#inverse of number
n=int(input())
r=0
while(n>0):
    
    remainder=n%10
    r=r*10+remainder
    n=n//10
print(r)
