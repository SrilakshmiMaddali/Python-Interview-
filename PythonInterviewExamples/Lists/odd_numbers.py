"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""
max_input=int(input("Enter max number"))
odd_numbers_list=[]
for i in range(max_input+1):
    if i%2!=0:
        odd_numbers_list.append(i)

print("Odd numbers:\n",odd_numbers_list)