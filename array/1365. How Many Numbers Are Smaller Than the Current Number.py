from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
            [1,2,3,1,2,5,10]

            create an arr with all ele 0, n = 100

            loop through the arr => with count ele and increament the no index by 1

            [0,1,1,1,1,1,1]


            arrMap=>
            1st n loop  [0,2,2,1,0,1,0,0,0,0,1]
            2nd n loop  [0,2,4,5,5,6,0,0,0,6,7]

                                    => 2n
            

        """

        arrayMap = [0] * 101

        for no in nums:     arrayMap[no] += 1

        for i in range(1,101):    arrayMap[i] += arrayMap[i-1]

        result = []
        for no in nums:    result.append(arrayMap[no - 1] if no > 0 else 0)

        return result


        