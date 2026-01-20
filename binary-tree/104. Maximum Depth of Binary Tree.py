# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], level: int) -> int:
            if node is None:
                return level
            return max(
                dfs(node.left, level + 1),
                dfs(node.right, level + 1)
            )

        return dfs(root, 0)
    
# BFS

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0

#         arr: Deque[dict] = deque([{"node": root, "level": 1}])
#         maxlevel = 1

#         while len(arr) > 0:
#             node_obj = arr.popleft()
#             node, level = node_obj["node"], node_obj["level"] + 1

#             if node.left:
#                 arr.append({"node": node.left, "level": level})
#                 maxlevel = level

#             if node.right:
#                 arr.append({"node": node.right, "level": level})
#                 maxlevel = level

#         return maxlevel
        