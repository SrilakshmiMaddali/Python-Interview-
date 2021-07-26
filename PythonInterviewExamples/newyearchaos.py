"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state. If anyone has bribed more than two people, the line is too chaotic to compute the answer.

Function Description

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):

int q[n]: the positions of the people after all bribes
Returns

No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.

Constraints

Subtasks

For  score
For  score

Sample Input

2
5
2 1 5 3 4
5
2 5 1 3 4
Sample Output

3
Too chaotic
Explanation

Test Case 1

The initial state:

pic1(1).png

After person  moves one position ahead by bribing person :

pic2.png

Now person  moves another position ahead by bribing person :

pic3.png

And person  moves one position ahead by bribing person :

pic5.png

So the final state is  after three bribing operations.

Test Case 2

No person can bribe more than two people, yet it appears person  has done so. It is not possible to achieve the input state.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)