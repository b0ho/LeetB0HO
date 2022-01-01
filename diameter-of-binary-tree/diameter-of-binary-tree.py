# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.rec(root)
        
        return self.ans
        
    def rec(self, root):
        if root == None:
            return -1

        left = self.rec(root.left)
        right = self.rec(root.right)
        self.ans = max(self.ans, left + right + 2)

        return max(left, right) + 1
    