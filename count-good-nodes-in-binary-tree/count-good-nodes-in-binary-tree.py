# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = self.isGoodNode(root, -10001)

        return res
    
    def isGoodNode(self, node: TreeNode, t_max: int) -> int:
        cnt = 0

        if not node:
            return 0

        if node.val >= t_max:
            cnt = 1
            t_max = node.val

        cnt += self.isGoodNode(node.left, t_max) + self.isGoodNode(node.right, t_max)

        return cnt