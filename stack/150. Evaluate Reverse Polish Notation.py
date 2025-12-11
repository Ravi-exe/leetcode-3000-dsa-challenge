from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
            example: 5 4 + 8 * 3 -
                op = ((5 + 4) * 8) - 3)
                
                "5 + 4 * 8 - 3"

        """

        stack = []
        
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "/":
                stack.append(int((1 / stack.pop()) * stack.pop()))
            elif i == "-":
                stack.append(- stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(i))

        return stack[0]
    