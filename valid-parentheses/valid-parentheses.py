class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"(" : ")", "[" : "]",  "{" : "}"}
        left = set(["(", "[", "{"])
        stack = []
        ans = True
        
        for i in s:
            if i in left:
                stack.append(i)
            elif stack and i == bracket[stack[-1]]:
                    stack.pop()
            else:
                return False
        
        if stack != []:
            ans = False
            
        return ans
    