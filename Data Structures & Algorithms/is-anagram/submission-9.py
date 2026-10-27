'''
Understand:
Given two strings return tru if they are anagrams of each other 

Plan:
sort them, then compare the values

Implement:

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        one=sorted(s)
        two=sorted(t)

        for i in range(len(one)):
            if one[i]!= two[i]:
                return False
        
        return True
        












