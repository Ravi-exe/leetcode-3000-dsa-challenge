


from typing import List
import math

class MinStack:

    def __init__(self):
        self._data: List[int] = []
        self._min = None

    def push(self, val: int) -> None: 
        self._min = self._min if self._min != None and self._min < val else val
        return self._data.append(val)
        

    def pop(self) -> None: 
        self._data.pop()
        

    def top(self) -> int: return self._data[-1]
        

    def getMin(self) -> int: return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
    
"""