"""
Given a list of size n, remove all even integers from it. Implement this solution in Python and see if it runs without an error.

"""

def remove_even(list):
    odds = []  # Create a new empty list
    for number in list:  # Iterate over input list
        # Check if the item in the list is NOT even
        # ('%' is the modulus symbol!)
        if number % 2 != 0:
            odds.append(number)  # If it isn't even append it to the empty list
    return odds  # Return the new list


print(remove_even([3, 2, 41, 3, 34]))
# time complexity is O(n)

# using list comprehension
def remove_even(list):
    # List comprehension to iter aover List and add to new list if not even
    return [number for number in list if number % 2 != 0]


print(remove_even([3, 2, 41, 3, 34]))
#The time complexity of this solution is also O(n), since only the syntax has changed while the algorithm still iterates over all elements of the list.
