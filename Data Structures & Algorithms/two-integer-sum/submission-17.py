'''
Understand:
given an array of integers, nums, and a target, 

return the indices i and j such that nums[i] + nums[j] == target.


i!=j.

Plan: 

first, make a hashmap, the key being the number, and the value being the index.

then, loop through nums, 

check if the complement of your number is already in the hashmap, cuz 
this would mean that i and j exist, and that i would be the index of the complement.

adding each value to the hashmap.
Implement: 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table={}

        for i in range(len(nums)): 
            complement=target-nums[i]

            if complement in table:
                return [table[complement],i]

            table[nums[i]]=i
















