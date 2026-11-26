# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque()
        levels = 0
        queue.append(root)

        while len(queue)>0:
            levels += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
        
        return levels