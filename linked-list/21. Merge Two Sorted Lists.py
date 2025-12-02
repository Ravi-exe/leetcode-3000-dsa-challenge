from typing import Optional


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


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            1,   2,   3,   4,   5,   6
            0,  4,  10,  21

            head -> None 
            tail

            1st occurence -> head -> 

            left merger
                left >= right , right is empty : left -> left.next
                right > left, left is empty:  rightNode extract , right = right.next, rightNode join left chain(frontside in leftNode)  
        """
        
        if list1 == None and list2 == None: return None

        left = list1
        right = list2

        head: ListNode | None 
        tail: ListNode | None = None
        if left != None and right != None:
                if left.val <= right.val:
                    current = left
                    left = left.next
                    head = current
                else:
                    current = right
                    right = right.next
                    head = current
                head.next = None
                tail = head
        elif left == None: return right
        else: return left

        while left != None or right != None:
            print(left, right, head, tail)
            if left != None and right != None:
                if left.val <= right.val:
                    current = left
                    left = left.next
                    tail.next = current
                else:
                    current = right
                    right = right.next
                    tail.next = current
                tail = current
                tail.next = None
            elif left == None:
                tail.next = right
                break
            else:
                tail.next = left
                break
        return head


ele1st = ListNode(val=1)
ele2st = ListNode(val=2)
ele3st = ListNode(val=3)
ele1st.next = ele2st
ele2st.next = ele3st
ele3st.next = None

print("listnode", ele1st, ele1st.val)

alterele1st = ListNode(val=4)
alterele2st = ListNode(val=5)
alterele3st = ListNode(val=6)
alterele1st.next = alterele2st
alterele2st.next = alterele3st
alterele3st.next = None

print("listnode", alterele1st)

solution = Solution()

result = solution.mergeTwoLists(ele1st, alterele1st)

print(result)


