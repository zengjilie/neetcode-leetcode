# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        visit = set()
        
        def bfs(r,c):
            q = collections.deque()  
            q.append((r,c))
            
            while q:
                r, c = q.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    if (r+dr in range(rows) and 
                        c+dc in range(cols) and
                        grid[r+dr][c+dc] == "1" and 
                        (r+dr, c+dc) not in visit):
                        q.append((r+dr, c+dc))
                        
                visit.add((r,c))
                
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    islands+=1
                    
        return islands

# time complexity O(rows*cols)
# space complexity O(rows*cols)