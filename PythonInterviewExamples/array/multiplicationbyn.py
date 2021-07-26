# Python3 program to
# find remainder when
# all array elements
# are multiplied.

# Find remainder of arr[0] * arr[1]
# * .. * arr[n-1]


arr= {100, 10, 5, 25, 35, 14}
n=11
multiple=1
for i in arr:
    multiple = multiple*i

print(multiple%n)