# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
reverse and return a linked list
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        lst=[]
        while curr: 
            lst.append(curr.val)
            curr=curr.next 
        lst=lst[::-1]

        curr=head
        i=0
        while curr:
            curr.val= lst[i]
            i+=1
            curr=curr.next 
        return head