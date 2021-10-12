class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[len(nums) - 1]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                Sum = nums[i] + nums[left] + nums[right]
                
                if abs(target - Sum) < abs(target - res):
                    res = Sum
                if Sum <= target:
                    left += 1
                else:
                    right -= 1
                
            
        return res