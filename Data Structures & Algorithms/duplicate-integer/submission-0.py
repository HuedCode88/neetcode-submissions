'''
Given an array of nums, return true if any value appears more than oncee


Plan: 
Create a hashmap storing the values of the array. While looping
through the array, constantly check if the current value is in the hashmap. 
if it is, return true, 
return false
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        for i in nums:
            if i in map: 
                return True
            else:
                map[i]=i
        return False