# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
            
        """

        if root == None: return False
        
        if root.val == subRoot.val:
        
            tempRoot = deque([(root, subRoot)])
            
            while tempRoot:
                
                n1, sn2 = tempRoot.popleft()
                
                if not n1 and not sn2:
                    continue
                if not n1 or not sn2:
                    return False
                if n1.val != sn2.val:
                    return False
                
                tempRoot.append((n1.left, sn2.left))
                tempRoot.append((n1.right, sn2.right))
            
            return True

        
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        )
        
