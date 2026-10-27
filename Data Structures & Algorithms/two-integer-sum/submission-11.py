'''
Understand:
given an array of integers nums and an integer target, return the indices i an j
if they ==target and i!=j

Match: 
two sum, answer uses the complement. 

Plan:
create a hashmap storing the values of nums and their indices 

then loop through nums: 
create the complement: 
complement = target - current. 

if the complement is in the hashmap, and the complement doesn't have the same index 
return [currentIndex,complementIndex]


Implement: 
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)): 
            comp = target-nums[i]
            if comp in map:
                return [map[comp],i]
            map[nums[i]]=i
   









        