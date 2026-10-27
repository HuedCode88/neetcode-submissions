class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
    
        Do not return anything, modify s in-place instead.
        """
        '''
        Understand: Given an array of strings, reverse it in O(1) time 

        plan: 
        two pointer:
        make two vars for the beginning and end of the array

        j=0
        k= len(s)-1

        then, swap the positions of values in those positions using a while loop
        need to have a temp variable to store the current j as well
        j=0
        k= len(s)
        while(j<k):
            temp=s[j]
            s[j]=s[k]
            s[k]=temp

            j+=1
            k-=1
        '''
        j=0
        k= len(s)-1
        while(j<k):
            temp=s[j]
            s[j]=s[k]
            s[k]=temp

            j+=1
            k-=1


        