from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        """

        result = []

        def recursion(output=0, arr=[], ind=0):

            for ind in range(ind, len(candidates)):
                no = candidates[ind]
                total = no + output

                if total == target:
                    result.append([*arr, no])
                    continue
                elif total > target:
                    continue

                recursion(total, [* arr, no], ind)

        recursion()

        return result
            