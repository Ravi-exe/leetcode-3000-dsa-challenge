
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack: List[str] = []
        openBracket = ["(","[","{"]
        closeMappedBracket = [")","]","}"]

        for i in s:
            for bracketInd, _ in enumerate(openBracket):
                # print(stack)
                if i == openBracket[bracketInd]:
                    stack.append(closeMappedBracket[bracketInd])
                if i == closeMappedBracket[bracketInd]:
                    if len(stack) == 0 or closeMappedBracket[bracketInd] != stack[-1]:
                        return False
                    stack.pop()
                

        # print(stack)
        return (True if len(stack) == 0 else False)