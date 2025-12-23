from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            O(n^2) time complexity, O(1) space complexity

            exmaple [-1,0,1,2,-1,7,9]

            combination => [-1,0,1,2,-1,7,9] = n (n -1) (n-2)  ~= n ^ 3, O(1)
                
                -1 0 1,     
                -1 0 2,     
                -1 0 -1,    
                -1 0 7,          
                -1 0 9,     

                -1 1 2,     0 1 2
                -1 1 -1,    0 1 -1
                -1 1 7,     0 1 7
                -1 1 9,     0 1 9

                -1 2 -1,    0 2 -1,    1 2 -1
                -1 2 7,     0 2 7,     1 2 7
                -1 2 9,     0 2 9,     1 2 9

                -1 -1 7,    0 -1 7     1 -1 7      2 -1 7
                -1 -1 9,    0 -1 9     1 -1 9      2 -1 9

                -1 7 9,     0 7 9      1 7 9       2 7 9       -1 7 9

            brute force => 
                    nested 3 loops and n^3 complexity
            
            method,
                using sort and unique array first=> n^2 + n ~= n ^2
                    then we can use two pointer for finding remaining result
                    [-1, 0, 1, 2, 7, 9]
            
            exception:
                [-5, -1, 0, 1, 2, 6]
        """
        result: List[List[int]] = []
        nums.sort()

        for ind , num in enumerate(nums):
            if num > 0: return result
            if ind > 0 and num == nums[ind - 1]: continue

            left=ind + 1
            right=len(nums) - 1
            pendingNum=0-num
            while left < right:
                res = nums[left] + nums[right]
                if res < pendingNum:
                    left+=1
                elif res > pendingNum:
                    right-=1
                else:
                    result.append([num, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result

soln = Solution()

print(soln.threeSum([-1,0,1,2,-1,7,9]))