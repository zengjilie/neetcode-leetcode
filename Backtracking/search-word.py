# https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        ans = False
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r not in range(row) or
                c not in range(col) or  
                (r,c) in path or
                word[i] != board[r][c]):
                return False
             
            path.add((r,c))
            
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r,c))
            return res
        
        #edge case, TLE if the count of the first letter > count of last letter
        if word.count(word[0]) > word.count(word[-1]):
            word = word[::-1]
                    
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
                    
# time complexity O(n^2)

# caveat
# Time Limit Exceed, need to reverse the string
# [
#     ["A","A","A","A","A","A"],
#     ["A","A","A","A","A","A"],
#     ["A","A","A","A","A","A"],
#     ["A","A","A","A","A","A"],
#     ["A","A","A","A","A","A"],
#     ["A","A","A","A","A","A"]
# ]
# "AAAAAAAAAAAAAAB"