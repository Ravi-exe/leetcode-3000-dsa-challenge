from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     current = 0
        #     while i < len(nums) and nums[i] == 1:
        #         current +=1
        #         i+=1
        #     count = count if count > current else current

        # return count

        count = [0,0]
        for i in nums:
            if i == 0: 
                count[0]= count[0] if count[0] > count[1] else count[1]
                count[1]= 0
            else: 
                count[1]+=1
        
        return count[0] if count[0] > count[1] else count[1]
