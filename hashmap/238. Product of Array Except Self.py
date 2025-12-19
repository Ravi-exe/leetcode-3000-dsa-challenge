from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            example,

                [1,2,3,4]

            1st way ,

                we will multiply all ele
                and loop in arrr
                and divide it with current ele nad append in result

                example => 
                    [1,2,3,4] product => 24

                    1st, 24/1 = 24 apppend
                    1st, 24/2 = 12 apppend
                    1st, 24/3 = 8 apppend
                    1st, 24/4 = 6 apppend

                result = 24,12,8,6

            2nd way , without division
                general [a,b,c,d]
                result = [b*c*d, a*c*d. a*b*d, a*b*c]
                product array = []
               
               [1,2,3,4]
                    product array left to right [1,2,6,24] and right to left [24,24,12,4]

                                         [1,2,12,4]
                                         a, a*b, c*d,d 
                    answer               [24,12,8,6]

                    a*b*c*d/ a

                pending
        """

        left = 1

        pref = [nums[left-1]]
        suff = [nums[-left]]

        while left < len(nums):
            pref.append(pref[left-1] * nums[left])
            suff.append(suff[left-1] * nums[-left-1])
            left+=1
        
        print(nums, pref, suff)

        result = [suff[-2]]
        for i in range(1, len(nums) -1):
            result.append(pref[i-1] * suff[-i-2])
        result.append(pref[-2])

        return result
    
soln = Solution()

print(soln.productExceptSelf([1,2,3,4,5,6]))

