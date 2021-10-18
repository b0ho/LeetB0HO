class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums) + 1):
            tmp = set(itertools.combinations(nums, i))
            res.update(tmp)
        
        return res