from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """

            [10,0,11,12,111,112,112,113,117,114,120,116,115,1000,11111]

            convert to set for 1 lookup 
             and check for 1+ number and del it if find

        """
        if len(nums) == 0: return 0
        longest = 1
        newSet = set(nums)
        for num in nums:
            if num - 1 in newSet:
                continue
            current = 1
            while num+1 in newSet:
                newSet.remove(num+1)
                current +=1
                num = num+1
            longest = longest if longest > current else current
        return longest

soln = Solution()

print(soln.longestConsecutive([2,20,4,10,3,4,5]))