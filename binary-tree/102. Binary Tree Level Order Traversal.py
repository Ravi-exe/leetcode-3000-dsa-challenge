# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:  return []
        arr =  deque([root])
        res = []

        while arr:
            
            tempArr = []
            for _ in range(len(arr)):
                node = arr.popleft()
                # if node: 
                tempArr.append(node.val)
                if node.left: arr.append(node.left)
                if node.right: arr.append(node.right)
                
            res.append(tempArr)
            
        return res
            
            