#https://www.educative.io/module/lesson/data-structures-in-python/N88v1y3PQA2


def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                my_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1



def find_second_maximum(lst):
    #Write your code here
    if (len(lst) <= 0):
        return None
    merge_sort(lst)  # sort list
    return lst[-2]

print(find_second_maximum([9,2,3,6]))
print(find_second_maximum([4,2,1,5,0]))

"""
Time Complexity #
The time complexity of this solution depends on the running time of sort() function. 
Assuming that Python sort() function runs in an optimal time of O(nlogn)O(nlogn), our solution also takes O(nlogn) time."
"""

#########################################################
def find_second_maximum(lst):
    lst.sort()
    if len(lst) >= 2:
        return lst[-2]
    else:
        return None


print(find_second_maximum([9, 2, 3, 6]))