from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
            target = [1,3], n = 3
            Output: ["Push","Push","Pop","Push"]

            target always increasing




        """
        ind=0
        result = []
        push="Push"
        pop="Pop"

        for no in range(1, n+1):
            print(no)
            if target[ind] == no:
                result.append(push)
                ind+=1
                if ind == len(target):
                    break
            else:
                result.append(push)
                result.append(pop)
        
        return result
    

soln = Solution()

print(soln.buildArray([1,3], 3))
print(soln.buildArray([4,5,6,9,10], 10))
print(soln.buildArray([1,3], 3))