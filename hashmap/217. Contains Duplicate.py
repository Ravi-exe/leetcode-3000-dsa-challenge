from typing import Dict, List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map: Dict[int, int]={}
        for i in nums:
            if map.get(i) != None:
                return True
            map[i] = 0
        return False
        