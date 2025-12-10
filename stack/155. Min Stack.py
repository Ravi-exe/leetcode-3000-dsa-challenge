


from typing import List
import math

class MinStack:
    """

        // embeding option study case
        stack  3, 1, 5,     -9
        
        min    3, 1, 1,     -9
        actual 0, -2, 4,    -10

        
        actual formula => val - min

        if actual negative means min change 
        if positive min not change 



    """

    def __init__(self):
        self._data: List[int] = []
        self._min : List[int] = []

    def push(self, val: int) -> None:
        self._data.append(val)
        self._min.append(self._min[-1] if len(self._min) > 0 and self._min[-1] < val else val)

    def pop(self) -> None:
        self._data.pop()
        self._min.pop()
        
    def top(self) -> int: return self._data[-1]
        

    def getMin(self) -> int: return self._min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
    
"""