"""
# Definition for a Node.
"""
from typing import Dict, Optional

class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        string = ""
        current = self
        while current:
            string += str(current.val)
            current = current.next
        return string



class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
            val, next, random,

 random =>  2  None,  5,  4,  3
            1,   2,   3,  4,   5
            copyPointer, realpointer

        """

        if head == None:  return None

        map: Dict[Node, Node] = {}
        current = head

        map[current] = Node(current.val)
        copiedHead: Node | None = map[current]
        copiedCurrent = copiedHead

        if current.random != None:
            if not current.random in map:
                map[current.random] = Node(current.val)
            copiedCurrent.random = map[copiedCurrent.random] #type: ignore


        current = current.next

        while current:
            map[current] = Node(current.val)

            copiedCurrent.next = map[current] 
            
            if current.random != None:
                if not current.random in map:
                    map[current.random] = Node(current.val)
                copiedCurrent.random = map[copiedCurrent.random] #type: ignore


            current = current.next
            copiedCurrent = copiedCurrent.next
            
        copiedCurrent.next = None
        # if current.random != None:
        #     if not current.random in map:
        #         map[current.random] = Node(current.val)
        #     copiedCurrent.random = map[copiedCurrent.random] #type: ignore


        return copiedHead
    

    
alterele_1 = Node(x=1)
alterele_2 = Node(x=2)
alterele_3 = Node(x=3)
alterele_4 = Node(x=4)
alterele_5 = Node(x=5)
alterele_6 = Node(x=6)
alterele_7 = Node(x=7)

alterele_1.next = alterele_2
alterele_2.next = alterele_3
alterele_3.next = alterele_4
alterele_4.next = alterele_5
alterele_5.next = alterele_6
alterele_6.next = alterele_7
alterele_7.next = None

print("listnode", alterele_1)
solution = Solution()
result = solution.copyRandomList(alterele_1)
print("reordered", result)
