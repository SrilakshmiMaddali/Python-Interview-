"""
Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are

"""

mystr ="""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

print(mystr)

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

###############################################################################################################

"""
Write a Python program to get the Python version you are using. Go to the editor
"""
import sys
print("Version: {}".format(sys.version))
print("Version Info: {}".format(sys.version_info))

#################################################################################################################

"""
Write a Python program to display the current date and time.
Sample Output : 
Current date and time : 
2014-07-05 14:34:14
"""

import datetime
print("Current date and time :")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

##################################################################################################################
"""
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output : 
r = 1.1
Area = 3.8013271108436504
"""
from math import pi
radius = float(input("r = "))
area = pi*(radius**2)
print("Area = {}".format(str(area)))

#############################################################################################################
"""
Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
"""
firstname = input("Enter First name: ")
lastname = input("Enter Last name: ")

print("{} {}".format(lastname,firstname))

##############################################################################################################

"""
Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
"""


values = input("Sample data: ")
mylist = values.split(",")
print("List : {}".format(mylist))
print("Tuple : {}".format(tuple(mylist)))

############################################################################################################

"""
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java 
Output : java
"""
import re
inputstr = input("Enter File name:")
print(re.search(r"\.([a-z]+)",inputstr))

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

#################################################################################################

"""
 Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
"""
color_list = ["Red","Green","White" ,"Black"]
print("First color : {}".format(color_list[0]))
print("Last color: {}".format(color_list[-1]))

#####################################################################################################
"""
 Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

"""

exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i"%exam_st_date )

########################################################################################################
"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5 
Expected Result : 615

"""

n = int(input("Enter n:"))
sum = n+(n*10+n)+(n*100+n*10+n)
print(sum)

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)