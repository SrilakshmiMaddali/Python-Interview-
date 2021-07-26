"""
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.

"""

print(abs.__doc__)
####################################################################

"""
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar
y = 2020 #int(input("Input the year : "))
m = 8 #int(input("Input the month : "))
print(calendar.month(y, m))

#########################################################################
"""
Write a Python program to print the following here document. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""

print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")

###########################################################################
"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
"""

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

##########################################################################
"""
Write a Python program to get the volume of a sphere with radius 6.
"""

from math import pi

radius = 6.0
volume = 4.0/3.0*pi*(radius**3)
print("Sphere Volume: {}".format(volume))

###########################################################################
"""
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. 
"""
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2

print(difference(22))
print(difference(14))

#########################################################################
"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""


def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

##########################################################################
"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.   
"""

def threesum(a,b,c):
    if a == b == c :
        return 3*(a+b+c)
    return a+b+c


print(threesum(2,2,2))
print(threesum(1,2,3))

#########################################################################
"""
Write a Python program to get a new string from a given string 
where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
"""

def getisword(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    return 'Is'+str

print(getisword('Ishikha'))
print(getisword('Kasyap'))

#########################################################################
"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""
def getnstr(str,n):
    if n>0 :
        return n*str

print(getnstr("Sri",3))

##########################################################################
"""
Write a Python program to find whether a given number (accept from the user) 
is even or odd, print out an appropriate message to the user.
"""
def evenorodd(num):
    result = ""
    if num%2 == 0:
        result = "Even number!"
    else:
        result= "Odd number!"
    return result

print(evenorodd(121))
print(evenorodd(120))

############################################################################
"""
 Write a Python program to count the number 4 in a given list. 
"""
def countfour(mylist):
    count=0
    for num in mylist:
        if num == 4:
           count+=1
    return count

print(countfour([4,12,13,14,4,4]))
print(countfour([1,2,2,3]))

############################################################################
"""
Write a Python program to get the n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2. 
"""
def getnewstring(str,n):
    if len(str)>2:
        return str[:2]*n
    return str*n

print(getnewstring("abc",4))
print(getnewstring("a",3))

##############################################################################
"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('a'))
print(is_vowel('r'))

################################################################################
"""
Write a Python program to check whether a specified value is contained in a group of values.
"""
def check(n,mylist):
    return n in mylist

print(check(4,[4,5,6,7]))
print(check(2,[3,4,5]))

#############################################################################
"""
Write a Python program to create a histogram from a given list of integers.
"""

def histogram(items):
    for item in items:
        print(item*'*')

histogram([2,3,6,5])

#############################################################################
"""
Write a Python program to concatenate all elements in a list into a string and return it.
"""

def concatenatelist(items):
    result = ""
    for item in items:
        result=result+item

    return result

print(concatenatelist(['hi','my','dear']))

###############################################################################
"""
Write a Python program to print all even numbers from a 
given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
Sample numbers list :

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]


"""

def printeven(items):
    for item in items:
        if item ==237:
            break
        if item % 2 == 0:
            print(item)

printeven([
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ])

#####################################################################################################
"""
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}
"""
def findlist(list1,list2):
    result=[]
    for item in list1:
        if item in list2:
            continue
        result.append(item)
    return result

print(findlist(set(["White", "Black", "Red"]),set(["Red", "Green"])))

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))

#####################################################################################################
"""
Write a Python program that will accept the base and height of a triangle and compute the area. 
"""
def area_triangle(b,h):
    return 1/2*b*h

print(area_triangle(20,40))

#######################################################################
"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers
"""
def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd


print(gcd(12, 17))
print(gcd(4, 6))
print(gcd(18,12))

##################################################################################
"""
Write a Python program to get the least common multiple (LCM) of two positive integers.
"""
def lcm(x,y):
    if x > y:
        z = x
    else:
        z = y

    while (True):
        if ((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

    return lcm
print(lcm(4, 6))
print(lcm(15, 17))

###########################################################################
"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""
def sum_three(x,y,z):

    if x==y or y==z or x==z:
        return 0
    return x+y+z

print(sum_three(2,2,3))
print(sum_three(10,20,30))

#########################################################################
"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
"""
def sum_two(x,y):
    sum=x+y
    if 15<sum<20:
        return 20
    return sum

print(sum_two(10,7))
print(sum_two(20,30))

##########################################################################
"""
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
"""
def gettrue(x,y):
    if x==y or x+y == 5 or x-y == 5:
        return True
    return False

print(gettrue(2,2))
print(gettrue(25,20))
print(gettrue(2,3))
print(gettrue(2,6))

##########################################################################
"""
Write a Python program to add two objects if both objects are an integer type.
"""
def findsum(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    return "Cant add "

print(findsum(2,3))
print(findsum('abc','2'))

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 20))

#######################################################################
"""
Write a Python program to display your details like name, age, address in three different lines.
"""
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()

######################################################################
"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""
def findsquare(x,y):
    result = (x+y)**2
    return result

print(findsquare(4,3))

#######################################################################
"""
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""
amt = 10000
int = 3.5
years = 7

future_value  = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

########################################################################
"""
 Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

###########################################################################
"""
Write a Python program to check whether a file exists.
"""
import os
open('abc.txt','w')
print(os.path.exists("abc.txt"))

##########################################################################
"""
Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
"""
import struct
print(struct.calcsize("P")*8)

#########################################################################
"""
Write a Python program to get OS name, platform and release information.
"""
import os
import platform
print(os.name)
print(platform.system())
print(platform.release())

#######################################################################
"""
Write a Python program to locate Python site-packages.
"""

import site
print(site.getsitepackages())

#######################################################################
"""
Write a python program to call an external command in Python.
"""
import subprocess
subprocess.call(['ls','-l'])

#####################################################################
"""
Write a python program to get the path and name of the file that is currently executing.
"""
import os
print("Current File Name : ",os.path.realpath(__file__))

####################################################################
"""
Write a Python program to find out the number of CPUs using.
"""
import multiprocessing
print(multiprocessing.cpu_count())

####################################################################
"""
Write a Python program to parse a string to Float or Integer.
"""
n = "246.2458"
print(float(n))
#print(int(float(n)))

##################################################################
"""
Write a Python program to list all files in a directory in Python. 
"""
#import subprocess
#print(subprocess.run(["ls","-la"]))

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home') if isfile(join('/home', f))]
print(files_list);

################################################################
"""
Write a Python program to print without newline or space.
"""
for i in range(0, 10):
    print('*', end="")
print("\n")

#################################################################
"""
Write a Python program to determine profiling of Python programs.
 A profile is a set of statistics that describes how often and for how long various parts of the program executed. 
 These statistics can be formatted into reports via the pstats module
"""







