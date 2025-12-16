from typing import List




class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            Input: temperatures = [30,  38,  30,  36,   35,   40,  28]
            
            Output: [1,4,1,2,1,0,0]

            input:  [30,38,30,36]

            #   [8,   -8,   6,  -1,  -5,    0,    0]
            it is an ordered 
            
            x = pop()

            modified array[8,-8,6] * jind - iind
                1  0 1 0
        
             
        case 36 25 22  28 
             36 22 28  40

        diff    11  3  -8

        
        """
        res= [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                lastInd, lastTemp = stack.pop()
                res[lastInd] = ind-lastInd
            stack.append((ind, temp))
        
        return res
    

soln = Solution()

print(soln.dailyTemperatures([30,  38,  30,  36,   35,   40,  28]))