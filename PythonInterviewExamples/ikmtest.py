s = "mary had a little little lamb"
for c in s[11:18]:
    print(c, end=' ')
    if "little" in c: print(c)

def genadd(x) :
    return lambda x,y : x + y

print(genadd)

tuple1 = "Online Testing", "Programming"
print(tuple1)

x, y = tuple1

print(x)
print(y)


def test(x):
    if x % 3 == 0:
        return test(x / 3)
    if x % 2 == 1:
        return x

    return test(2 * x + 1)

print(test(100))

num = [1, 2, 3, 4]
result = []

for x in num:
  result.append(x**2)

print(result)

x = isinstance('34\xc2\xb0', str)
y = 'abc'.encode().decode('ascii')
z = "".join(['34\xb0', "56'", '12.63"', 'S'])
w = "a" + "b"
print(x, y, z, w)


services = {"Service": "Python Testing", "Version": 3,"Results": 95}

print("Service : %s" %services["Service"], services["Version"],services["Results"])

services = {"Service": "Python Testing", "Version": 2,"Results": 95}

print("Service : %s" %services["Service"])
print("Version : %d" %services["Version"])
print("Results : %s" %services["Results"])


import sys
print ("enter user input")
line = sys.stdin.readline()

import inspect
import threading
for name, obj in inspect.getmembers(threading, inspect.isclass):
    print(name)

n = 12
names = [[]] * n
employee = "Adam"
m = 6
names[m].append(employee)
print(names)

