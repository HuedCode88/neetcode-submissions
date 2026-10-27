class Solution:
    '''
    given an integer array nums, rotate the array to the right 
    by k steps, where k is non-negative


    Understand: 
    
    Plan: 
    '''
    def rotate(self, nums: List[int], k: int) -> None:
        if k ==0:
            return nums
        Q=k%len(nums)
        new= nums[len(nums)-Q:]
        new+=nums[:len(nums)-Q]

        for i in range(len(nums)):
            nums[i]=new[i]
        