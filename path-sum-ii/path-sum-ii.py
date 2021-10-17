# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        
        self.dfs(root, targetSum, 0, [], res)
        
        return res
    
    def dfs(self, root:TreeNode, targetSum:int, tmpSum:int, tmpList:list, res:list):
        if not root:
            return
        
        tmpSum += root.val
        tmpList.append(root.val)
       
        if tmpSum == targetSum and root.left == None and root.right == None:
            res.append(tmpList[:])
        
        self.dfs(root.left, targetSum, tmpSum, tmpList, res)
        self.dfs(root.right, targetSum, tmpSum, tmpList, res)
        
        tmpList.pop()
        