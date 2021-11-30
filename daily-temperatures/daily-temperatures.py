class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))]
        stack = []
        
        for i in reversed(range(len(temperatures))):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        
        return ans
    