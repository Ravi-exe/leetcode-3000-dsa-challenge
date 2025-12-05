"""
# Definition for a Node.
"""
from typing import Optional

class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
            1,2,3,4,5
            val,
            next, 
            random


        """
        if head == None:  return None

        map = {}

        current = head
        newHead: Node | None = Node(current.val)
        
        current = head.next

        while current:
            
            if current.next == None:
                pass
            else:
                if current in map:
                    newHead.next = Node(current.val)
                else:
                    
                    newHead.next = Node(current.val)

            current = current.next


        return newHead