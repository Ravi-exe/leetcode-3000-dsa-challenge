from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

            example: [2,1,5,6,2,3]

                              __
                           __|  |
                          |  |  |
                          |  |  |   __
                     __   |  |  |__|  |
                    |  |__|  |  |  |  |
                    |  |  |  |  |  |  |
                      2  1  5  6  2  3

                for,
                    2 => 2 
                    21 => ... 1, 2(t)
                    215 => ... 5, 2, 3(t)

                
        """
        pass