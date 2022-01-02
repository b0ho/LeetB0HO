# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        ans = self.rec(root.left, root.right)
        
        return ans
    
    def rec(self, left, right):
        if left == None and right == None:
            return True
        if left == None and right != None:
            return False
        if left != None and right == None:
            return False
        if left.val != right.val:
            return False
        ret = self.rec(left.left, right.right) and self.rec(left.right, right.left)
        
        return ret
    