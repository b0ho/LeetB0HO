class Solution:
    def findIntegers(self, n: int) -> int:
        arr = bin(n)[2:][::-1]
        dp = [[1, 1] for _ in range(len(arr))]
        res = 2
        if arr[0] == '0':
            res = 1
        
        for i in range(1, len(arr)):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]
            
            if arr[i - 1:i + 1] == '01':
                res += dp[i][0]
            elif arr[i - 1:i + 1] == '11':
                res = dp[i][0] + dp[i][1]
                
        return res