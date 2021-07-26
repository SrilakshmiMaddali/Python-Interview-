"""
Implement a function right_rotate(lst, k) which will rotate the given list by k.
This means that the right-most elements will appear at the left-most position in the list and so on.
You only have to rotate the list by one element at a time.
"""

def right_rotate(lst, k):
    #Write your code here
    for i in range(k):
        next=lst[-1]
        for j in range(len(lst)):
            if j<len(lst)-1:
                next = lst[j+1]
                lst[j+1]=lst[j]
            else:
                lst[0]=next
    return lst



print(right_rotate([10,20,30,40,50],1))
