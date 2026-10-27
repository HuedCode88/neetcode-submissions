'''
Understand: given arr of length n,create an array ans of length 2n. 

ans[i]==nums[i] 

and ans[i+n]==nums i

'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]

        ans+=nums
        ans+=nums

        return ans
        
