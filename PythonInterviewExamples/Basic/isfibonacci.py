import math


def isperfect_square(x):
    s=int(math.sqrt(x))
    return s*s == x


def is_fibonacci(n):
    return isperfect_square(5*n*n + 4) or isperfect_square(5*n*n - 4)


print(is_fibonacci(8))
print(is_fibonacci(4))