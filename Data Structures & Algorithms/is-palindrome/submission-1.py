'''
Understand:
given a string, return if it's a palindrome, 
meaning return if it reads the same from front to back 

Plan: 
use a two pointer and a while loop, like this 

i=0
j=len(s)

while i<j: 
    if s[i]!=s[j]:
        return false
return true
Implement:

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:      
        new = ""
        for i in s: 
            if i.isalnum():
                new+=i.lower()
        
        i=0
        j=len(new)-1

        print(new)
        while i<j:
            if new[i]!=new[j]:
                return False
            
            i+=1
            j-=1
        return True

        








        