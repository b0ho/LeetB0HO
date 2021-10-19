class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
                    
        def dfs(x, y):
            visited.add((x,y))
            areas[idx] += 1
            
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < n and 0 <= new_y < n:
                    if not grid[new_x][new_y]:
                        arr[(new_x,new_y)].add(idx)
                    elif (new_x, new_y) not in visited:
                        dfs(new_x, new_y)
                        
        visited = set()
        arr = defaultdict(set)
        n = len(grid)
        res = 0
        idx = 0
        areas = [0] * (n * n)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    idx += 1
        
        if max(areas) == n * n:
            return n * n
        
        for i in arr:
            res = max(res, sum(areas[_] for _ in arr[i]))
            
        return res + 1
    