# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            1, 2, 3, 4, 5 
            |           |
        """
        if head == None: return False
        
        slow_pointer: ListNode | None = head.next

        if slow_pointer == None:
            return False
             
        fast_pointer: ListNode | None = slow_pointer.next

        while fast_pointer != None:
            if slow_pointer is fast_pointer: return True
            slow_pointer = slow_pointer.next # type: ignore
            fast_pointer = fast_pointer.next
            if fast_pointer == None: break
            fast_pointer = fast_pointer.next
        return False

