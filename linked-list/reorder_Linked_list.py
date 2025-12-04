
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
            1, 2, 3, 4, 5, 6, 7, 8, 9

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
        fast = slow.next
        if fast == None: return None
        fast = fast.next
        # if fast == None:  return None
        
        # current: ListNode | None = None
        found_last_node = False
        arr: List[ListNode] = []

        while slow != None:
        
            if found_last_node == False:
                node = fast.next 
                if node == None: # even
                    found_last_node = True
                elif node.next == None: # odd
                    found_last_node = True
                    # current = fast
            else:
                node = arr.pop()
                node.next = slow
                slow.next = fast
                fast = node
                
            arr.append(slow)
            slow = slow.next
            print()

alterele1st = ListNode(val=4)
alterele2st = ListNode(val=5)
alterele3st = ListNode(val=6)
alterele1st.next = alterele2st
alterele2st.next = alterele3st
alterele3st.next = None

print("listnode", alterele1st)
solution = Solution()
result = solution.reorderList(alterele1st)
print(result)


