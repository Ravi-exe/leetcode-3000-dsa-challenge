from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            list of linked list [[10,11][1,2,4],[1,3,5],[3,6]]
            
            while -> 
             i = 0
                1,1,3,10

        
            
        """

        obj = {}

        for i in lists:
            pass