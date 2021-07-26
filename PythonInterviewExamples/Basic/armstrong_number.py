import math
def order(x):
    n=0
    while (x!=0):
        n=n+1
        x=x//10
    return n


def find_armstrong(x):
    n=order(x)
    temp = x
    sum1 = 0
    while(temp!=0):
        r=temp%10
        sum1+=math.pow(r,n)
        temp = temp//10
    return sum1 == x

print(find_armstrong(153))
print(find_armstrong(1634))