def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b

def find_fibonacci(n):
    for index,i in enumerate(fibonacci()):
        if index == n-1:
            print(i)

print(find_fibonacci(9))