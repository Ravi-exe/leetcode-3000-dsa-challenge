

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            [1,2,2,11,1,1,1,10]
            
            ele, rank, score, 
            ele freq
            score update
            rank manipulte

            score{
                1: (4, 1 (1st ind of rank))
                2: (3, 2 (1st ind of rank))
                3: (2, 3 (1st ind of rank))
                4: (1, 4 (1st ind of rank))
            }
            rank [1th,2th,3th,4th]
                   1,  2, 3,  4,



        """
        rank = []
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
            # if map[i
            
        return [rank[i] for i in range(k)]