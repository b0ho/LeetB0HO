class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:       
        nums2 = set(nums)
        ans = []
        
        for i in range(1, len(nums)+1):
            print(i)
            if i not in nums2:
                ans.append(i)
        
        return ans