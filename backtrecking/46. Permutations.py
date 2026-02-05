from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        
                1, 2, 3, 4, 5, 6, 7, 8
                2-n 
                
        """
        
        result = []
        def recurse(temp_nums=nums, arr=[]):

            if len(temp_nums) == 0:
                result.append(arr)
                return

            for ind, num in enumerate(temp_nums):
                recurse([*temp_nums[0:ind], *temp_nums[ind+1:]], [*arr, num])

        recurse(nums)
        return result

