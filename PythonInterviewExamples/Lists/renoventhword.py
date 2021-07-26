"""
Input: list - ["geeks", "for", "geeks"]
       word = geeks, N = 2
Output: list - ["geeks", "for"]

"""
word_list = ["geeks","for","geeks"]
nth =2
word1 = "geeks"
count =0
for i in range(len(word_list)):
    if word_list[i] == word1:
        count+=1
        if count==2:
            del(word_list[i])
print(word_list)

