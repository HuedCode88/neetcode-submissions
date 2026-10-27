'''
Understand:
given two strings return true if they are anagrams of each other

an anagram being a string that contains the same characters but in a different order


Plan:
base cases
if s==t:
    return False because they're the same 
if s<t 
or 
if s>t 
return false 

create a hashmap 
loop through s, assigning each value its count

then, make another map. loop through t. doing the same.
but if any values are not in map1, return false. and if the count is > the count in the other, return false.
Implement:

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s==t and len(s)==1:
            return True
        if s == t:
            return False
        if len(s)<len(t) or len(s)>len(t):
            return False

        map1={}
        map2={}
        for i in s:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        for i in t:
            if i not in map1:
                return False
            if i in map2:
                map2[i]+=1
                if map2[i]>map1[i]:
                    return False
            else: 
                map2[i]=1
        
        return True
        












