"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""

def twosum(mylist,target):
    for index,i in enumerate(mylist):
        diff = 0
        tarindex = 0
        if i < target:
            diff = target - i
            if diff in mylist:
                tarindex = mylist.index(diff)
                return index,tarindex
                break


print(twosum([2,7,8,9,10],9))

print(twosum([2,3,4,5,6],10))


#####################################################################


"""
Add Two Numbers
Medium

8437

2142

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

########################################################################
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def find_longstring(text):
    mylist=[]
    str = ""
    for i in text:
        if i not in str:
            str=str+i

    mylist.append(str)
    print(mylist)
    largest=""
    for i in mylist:
        if len(largest) < len(i):
            largest = i

    return largest

print(find_longstring('abcabcabc'))
print(find_longstring('bbb'))
print(find_longstring('pwwkew'))

str ="ABC".encode('utf-8')
print(str)
print(str[-1])

my_map = {'a': 1, 'b': 2}
inv_map = {y:x for x,y in my_map.items()}
print(inv_map)

"Providing two lists, first list is name of color such as [red, green, blue]," \
" and second list is animals such as [dog, cat]. " \
"Can you generate their combinations [red cat, red dog, blue cat, …]"
list_a=["red", "green", "blue"]
list_b=["dog", "cat","rabbit"]
c = [x+" "+y for x in list_a for y in list_b if x[0]!=y[0]]

print(c)

print(eval('list'))
inventory = [("ford", 33), ("honda", 15), ("nissan", 23), ("volvo", 4), ("kia", 12)]
for i in [make for make, num in enumerate(inventory) if num[1] > 12]:
     print(inventory[i][0])

lim = 12
for c in inventory:
        try:
                if c.index(c[1]) > lim:
                        print( c[0])
        except ValueError:
                pass

class Foo(object):
    def class_foo(cls):
        print("Class method for the class: %s" % cls)
    class_foo = classmethod(class_foo)
Foo.class_foo()

class Foo(object):
    @classmethod
    def class_foo(cls):
        print("Class method for the class: %s" % cls)
Foo.class_foo()





x = 1
y = 0
z = 0
result = 2
try:
    z = z + 1
    result = x / y
    z = z + 1
except ZeroDivisionError:
    z = z + result
else:
    z = z + 1
finally:
    z = z + 1
z = z + 1
print(z)

list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output = []

for x in list:
    if x % 2 == 0:
        output.append(x)

print("Output list:", output)


class gen_bytes(object):
    def __init__(self):
        acc_log = open("access.log")
        self.num = 0
        self.lines = acc_log.readlines()
        self.len = len(self.lines)
    def __iter__(self):
        return self
    def next(self):
        if self.num < self.len:
            line = self.lines[self.num]
            bytes_str = line.rsplit(None,1)[1]
            return int(bytes_str)
        else:
            raise StopIteration()

print("Bytes total:", sum(gen_bytes()))


s = "mary had a little little lamb"
for c in s[11:18]:
    print(c, end=' ')
    if "little" in c: print(c)

