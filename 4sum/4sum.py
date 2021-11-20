class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        nums.sort()
        
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        if (nums[i], nums[j], nums[k], nums[l]) not in answer:
                            answer.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
                
        return list(answer)