from typing import List, cast


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # if nums[0] != 1: return [nums[0], 1]
        # if nums[-1] != len(num) - 1: return [nums[-1], len(num) -1]

        map = {}
        duplicateValue: int = 0
        total = cast(int,(len(nums) + 1) * len(nums)/2)
        for no in nums:
            if no in map:  
                duplicateValue = no
                continue
            map[no] = 0
            total -=no
    
        return [duplicateValue, total]