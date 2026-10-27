'''
Understand:
Given Two Strings s and t return true if they are anagrams of eachother.
if not, return false.

Plan:
check if they're the same length, if not immediately return false.


sort em, then loop over one and check it against the other

Implement:

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s2 = sorted(s)
        t2 = sorted(t)
        
        for i in range(len(s2)):
            if s2[i]!=t2[i]:
                return False
        return True
        












