'''
Understand: given arr of length n,create an array ans of length 2n. 

ans[i]==nums[i] 

and ans[i+n]==nums i

Plan: 

this problem is very simple. it's just asking you to create an array with the
array happening twice basically. You can do that by using python's innate concatenation. 
'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]

        ans+=nums
        ans+=nums

        return ans
        
