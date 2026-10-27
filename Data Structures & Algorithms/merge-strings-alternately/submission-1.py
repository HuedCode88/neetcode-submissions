'''
Understand:
given word1 and word2, make a new string merging them letter by letter

Plan: 
using a while loop, loop through the strings for len and add them
to a temp string

'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string=""
        cnt1=0
        cnt2=0

        while cnt1<len(word1) or cnt2<len(word2):
            if cnt1<len(word1):
                string+=word1[cnt1]
                cnt1+=1
            if cnt2<len(word2):
                string+=word2[cnt2]
                cnt2+=1
        return string