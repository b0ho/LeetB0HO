class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        res = False
        Alex = 0
        Lee = 0
        piles.sort()
        
        left = 0
        right = len(piles) - 1
        
        while left != right:
            print(left, right)
            if (piles[left] > piles[right]):
                Alex += piles[left]
                left += 1
            else:
                Alex += piles[right]
                right -= 1
            
            if left == right:
                break;
            
            if (piles[left] > piles[right]):
                Lee += piles[right]
                right -= 1
            else:
                Lee += piles[left]
                left += 1
        
        if Alex > Lee:
            res = True
            
        return res