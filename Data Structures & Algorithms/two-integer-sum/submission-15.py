'''
Understand:
given an array of numbers, and a target integer,

return the indices of numbers that add up to the target value 

Plan:
loop through the thing, set the indices as the values and the key as the current.
every loop, subtract the current value from target, because the "match" will 
end up being the complement of the current value
Implement: 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table={}

        for i in range(len(nums)):
            complement = target-nums[i]

            if complement in table: 
                return [table[complement],i]

            table[nums[i]]=i




