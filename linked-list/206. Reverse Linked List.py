

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None: return None
        
        prevNode: ListNode | None = None
        currentNode: ListNode | None = head
        nextNode: ListNode | None = head
        
        # if nextNode == None: return head
        while currentNode != None:
            nextNode = nextNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode

        return prevNode
        
        
# testing 
# for now not adding testing . will be adding in future 
# solution = Solution()
# assert solution.reverseList()
        
