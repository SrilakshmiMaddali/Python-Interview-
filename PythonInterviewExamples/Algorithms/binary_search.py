def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    complexity of this is o(log n) which is less time compared to o(n) or o(n2)
    it takes less number of rotations to find the number
    """

    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1