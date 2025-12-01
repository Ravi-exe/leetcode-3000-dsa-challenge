
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map: Dict[int, int] = {}
        for ind, value in enumerate(nums):
            map[value] = ind
        for ind, value in enumerate(nums):
            remain = target - value
            if map.get(remain) != None and map.get(remain) != ind:
                return [ind, map[remain]]
        return []
    