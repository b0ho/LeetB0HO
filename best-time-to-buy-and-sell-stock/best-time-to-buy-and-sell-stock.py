class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mini = prices[0]
        
        for i in prices:
            ans = max(ans, i - mini)
            mini = min(i, mini)
            
        return ans
    