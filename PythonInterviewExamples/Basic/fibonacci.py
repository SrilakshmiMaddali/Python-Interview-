def fibonacci():
    a,b=1,1
    while True:
        yield a
        a,b = b,a+b


for index, x in enumerate(fibonacci()):
    if index == 10:
        break
    print("%s" % x,end=" ")
