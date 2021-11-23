# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        ans = self.getDepth(root, 0, 0)
        
        print(ans)
        
        return ans
    
    def getDepth(self, root: Optional[TreeNode], depth: int, max_depth: int) -> int:
        if root == None:
            return max_depth
        
        depth += 1
        if max_depth < depth:
            max_depth = depth
        
        if root.left != None:
            max_depth = self.getDepth(root.left, depth, max_depth)
        if root.right != None:
            max_depth = self.getDepth(root.right, depth, max_depth)
        
        return max_depth