class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        ans = max(dic, key = dic.get)
        
        return ans