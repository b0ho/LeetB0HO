# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        now = root

        while now:
            left = now.left
            if left:
                while left.right:
                    left = left.right
                left.right = now.right
                now.right = now.left
                now.left = None
            now = now.right

        return root