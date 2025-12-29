from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for no in nums:
            ind= abs(no) - 1
            nums[ind] = -abs(nums[ind])

        for ind, ele in enumerate(nums):
            if ele > 0: result.append(ind+1)

        return result
        
        