class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, sub):
            ans = False
            
            if root == None: 
                return False
            
            if k - root.val in sub: 
                return True
            
            sub.add(root.val)
            
            ans = dfs(root.left, sub) or dfs(root.right, sub)
            
            return ans
        
        return dfs(root, set())