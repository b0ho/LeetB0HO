class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(num):
            return (int(num**0.5))**2 == num
        
        if is_square(n):
            return 1
        
        for i in range(int(n**0.5) + 1):
            if is_square(n - i**2):
                return 2
            
        for i in range(int(n**0.5) + 1):
            for j in range(int(n**0.5) + 1):
                if (n - i**2 - j**2) < 0:
                    break
                elif is_square(n - i**2 - j**2):
                    return 3	
                
        return 4