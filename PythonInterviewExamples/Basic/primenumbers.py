def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count==2

def printprime(x,y):
    for i in range(x,y):
        if isprime(i):
            print(i)


print(printprime(1,20))

print(printprime(11,25)) 