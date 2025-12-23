from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for i in range(n) for x in (nums[i], nums[i+n])]
        # for i in range(n):
        #     result.append(nums[i])
        #     result.append(nums[])