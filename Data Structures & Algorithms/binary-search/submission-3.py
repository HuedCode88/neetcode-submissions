'''
Given a list of nums sorted in ascending order, and an integer target
find it in (Ologn time)



Binary Search! 

left=0
right = len(nums)

while(left<right):
    mid=(left+right)/2
    if nums[mid]==target:
        retun mid
    if nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
return -1

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left=0
        right = len(nums)-1

        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

