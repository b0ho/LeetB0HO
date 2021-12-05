class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        tmp = 1
        for n in nums:
            ans.append(tmp)
            tmp *= n

        tmp2 = 1
        for i in reversed(range(len(nums))):
            ans[i] *= tmp2
            tmp2 *= nums[i]
            
        return ans
    