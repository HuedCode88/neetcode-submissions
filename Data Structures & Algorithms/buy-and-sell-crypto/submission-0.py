'''
given an int array prices, 
where prices[i] is the price of a coin on ith day. 

choose a single day to buy 1 coin 
and a single day in the future to sell it. 

return max profit. 



plan: 
bc on a timeline  

two pointer. 
L 
R 

maxP

L=0
R=1
maxP=0

while(R<len(prices)):
    if prices[L]<prices[R]:#Profitable
        profit=prices[R]-prices[L]
        maxP= max(profit,maxP)
    #if L>R, reassign L to be the right, and R+=1
    else: 
        L=R
    R+=1
return maxP



'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        L=0
        R=1
        maxP=0

        while(R<len(prices)):
            if prices[L]<prices[R]:#Profitable
                profit=prices[R]-prices[L]
                maxP= max(profit,maxP)
            #if L>R, reassign L to be the right, and R+=1
            else: 
                L=R
            R+=1
        return maxP








            