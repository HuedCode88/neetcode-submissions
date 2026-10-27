'''
Understand:
given two strings, s and t, return true if they are anagrams of each other 

Plan:
check if they are the same length, cuz if not, couldn't be one. 

then, if you sort them, and then check them index by index, you'll find out 
if they're still anagrams 


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s2=sorted(s)
        t2=sorted(t)

        for i in range(len(s2)): 
            if s2[i]!=t2[i]:
                return False
        
        return True












