##The time complexity of this code is O(n^2)O(n2​​ ). Again, this algorithm is not very efficient.
def selection_sort(lst):
    """
      Selection sort function
      :param lst: List of integers
      """


    for i in range(len(lst)):
        min_index=i
        for j in range(i+1,len(lst)):
            if lst[min_index]>lst[j]:
                min_index=j

        lst[i],lst[min_index]=lst[min_index],lst[i]

# Driver code to test above
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)

"""
https://www.educative.io/courses/algorithms-coding-interviews-python/B62q79Pn2AJ
This algorithm works by repeatedly finding the minimum element in the list and placing it at the beginning. This way, the algorithm maintains two lists:

the sublist of already-sorted elements, which is filled from left to right
the sublist of the remaining unsorted elements that need to be sorted
In other words, this algorithm works by iterating over the list and swapping each element with the minimum (or maximum) element found in the unsorted list with that in the sorted list.
"""