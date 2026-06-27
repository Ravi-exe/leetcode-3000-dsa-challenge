from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        def recursion(nums, index=0,tempResult=[]):
            for ind in range(index, len(nums)):
                tempResult.append(nums[ind])
                result.append(tempResult.copy())
                recursion(nums, ind+1, tempResult.copy())
                tempResult.pop()
        
        recursion(nums)
        return result
            
 
 