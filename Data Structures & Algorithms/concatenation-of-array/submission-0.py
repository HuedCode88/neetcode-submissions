'''
understand
given an array nums of length n
create an array ans of length 2n 
where ans[i]==nums[i] and ans[i+n]==nums[i] 

for 0<=i<n 
plan 

start by making an array
arr=[]
then
looping twice, add all values of nums to ans with a nested for loop.

'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[]
        for j in range(2):
            for i in nums:
                arr.append(i)     
        return arr