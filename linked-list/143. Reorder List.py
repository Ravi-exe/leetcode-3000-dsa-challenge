
# Definition for singly-linked list.
from typing import List, Optional


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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
            1, 2, 3, 4, 5, 6, 7, 8, 9

            1,2,3,4,5 
            1,3,5,7,9 

            

            for 2 times scanning method=> 

            [9,8,7,6,5,4,3,2,1] 1st scan crete a stack ds 
                using stack ds of pointer if next ele is equal to current we stop loop and returns it
            
            [1, 2, 3, 4, 5, 6, 7, 8, 9] 1st scan map of ind and pointer to the particular indexed node
                using indexed mapping array we will create a relation by formula : i: length -i -1

            for one time scanning
            
                1, 2, 3, 4, 5, 6, 7, 8

                slow 
                        1 2 3 4 5
                fast 
                        3 5 7 8 None 

                    conclusion, length -> 8, ith 4

                pairing 
                    4-> 5 -> None, 4
                    3-> 6 -> 4, 3
                    2 -> 7 -> 3 , 2
                    1 -> 8, 1 

                        result -> 1 -> 8, 2 -> 7, 3 -> 6, 4 -> 5 -> None

        """
        
        if head == None: return None

        slow = head
        fast = slow
        # if fast == None: return None
        # fast = fast.next
        # if fast == None:  return None
        
        # current: ListNode | None = None
        found_last_node = False
        arr: List[ListNode] = []
        current: ListNode | None = None

        while slow != None:
            if found_last_node == False: 
                print(found_last_node,slow, arr)
                if fast == None: # even
                    found_last_node = True
                elif fast.next == None: # odd
                    found_last_node = True
                    current=slow
                    slow=slow.next
                    current.next = None
                    # fast = node.next
                else:
                    fast = fast.next.next
                    arr.append(slow)
                    slow = slow.next
            else:
                # print(found_last_node,slow, arr)
                nextNode = slow.next
                node = arr.pop()
                node.next = slow
                slow.next = current
                current = node
                slow = nextNode


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
result = solution.reorderList(alterele_1)
print("reordered", alterele_1)

