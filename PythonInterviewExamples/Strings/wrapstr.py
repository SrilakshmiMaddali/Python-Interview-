"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import textwrap

#def wrap(string, max_width):
    #mylist = textwrap.wrap(string,max_width)
    #return mylist
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    dedented_text = textwrap.dedent(text=string)
    result = wrapper.fill(text=dedented_text)
    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)