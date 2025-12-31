


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            Input: prices = [7,1,5,3,6,4]
            Output: 5
            
            
            
        """
        if len(prices) == 1: return 0
        
        left = 0
        right = 1
        cost = 0  
        
        # if prices[left] > prices[right]:
        #     cost = prices[left] - prices[right]
        #     left = right
        #     right +=1
        # else:
            
        
        while right < len(prices):
            if prices[right] > prices[left]:
                currentCost = prices[right] - prices[left]
                cost = cost if cost > currentCost else currentCost
            else:
                left = right
            right +=1
            
        return cost