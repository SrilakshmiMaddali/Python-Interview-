"""

1. Given S = "abccbd" and C = [0, 1, 2, 3, 4, 5], the function should return 2. You can delete the  rst occurrence of 'c' to achieve "abcbd".
2. Given S = "aabbcc" and C = [1, 2, 1, 2, 1, 2], the function should return 3. By deleting all letters with a cost of 1, you can achieve string "abc".
3. Given S = "aaaa" and C = [3, 4, 5, 6], the function should return 12. You need to delete all but one letter 'a', and the lowest cost of deletions is 3+4+5=12. 4. Given S = "ababa" and C = [10, 5, 10, 5, 10], the function should return 0. There is no need to delete any letter.
4.Given S = "ababa" and C = [10, 5, 10, 5, 10], the function should return 0. There is no need to delete any letter.
"""
def solution(S,C):
# write your code in Python 3.6 total_cost = 0
    i=0
    total_cost=0

    while i < (len(S)-1):
        if S[i]==S[i+1]:
            if C[i]<=C[i+1]:
                total_cost+=C[i]
            elif C[i]>C[i+1]:
                total_cost+=C[i+1]
            else:
                total_cost += C[i]
            print(C[i])
        i += 1
    return total_cost



#print(solution('abccbd',[0, 1, 2, 3, 4, 5]))
#print(solution('aabbcc',[1, 2, 1, 2, 1, 2]))
#print(solution('aaaa',[3, 4, 5, 6]))
#print(solution('ababa',[10, 5, 10, 5, 10]))
print(solution('aaabbb',[1,2,3,3,1,2]))
#print(solution('aaaaaa',[1,2,3,0,4,6]))
