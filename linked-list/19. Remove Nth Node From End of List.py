# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def __str__(self):
        string = ""
        current = self
        while current:
            string += str(current.val)
            current = current.next
        return string
    
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            1, 2, 3, 4, 5, 6, 7
            | - n+1 - |  

            take two pointer diff between them will be n
            once last pointer reach .. we will remove first pointer address
        """
        # global prevNode
        if head == None: return head
        current = head
        ind = 1
        prevNode = None
        while current:
            print(prevNode)

            if ind == n + 1: 
                prevNode = head
                ind+=1

            if current.next == None :
                if prevNode == None:
                    newHead = head.next
                    head.next = None
                    head=newHead
                else:
                    nextNode = prevNode.next.next # type: ignore
                    prevNode.next.next = None # type: ignore
                    prevNode.next = nextNode # type: ignore
                    break

            if prevNode != None: 
                prevNode = prevNode.next
            else: ind += 1
            current = current.next

        return head



alterele_1 = ListNode(val=1)
alterele_2 = ListNode(val=2)
alterele_3 = ListNode(val=3)
alterele_4 = ListNode(val=4)
alterele_5 = ListNode(val=5)
alterele_6 = ListNode(val=6)
alterele_7 = ListNode(val=7)


alterele_1.next = alterele_2
alterele_2.next = alterele_3
alterele_3.next = alterele_4
alterele_4.next = alterele_5
alterele_5.next = alterele_6
alterele_6.next = alterele_7
alterele_7.next = None

print("listnode", alterele_1)
solution = Solution()
result = solution.removeNthFromEnd(alterele_1, 7)
print("removeNthFromEnd", result)

