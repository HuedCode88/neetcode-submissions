'''
given nums, return true if something happens more than once. otherwise false

plan: 
make a hashmap and check every value against it. 
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        for i in nums:
            if i in map: 
                return True
            else: 
                map[i]=1
        return False