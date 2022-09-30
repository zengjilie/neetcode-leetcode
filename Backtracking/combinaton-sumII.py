# https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res = []
        
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i == len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            backtrack(i+1, cur, total + candidates[i])
            
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, cur, total)
            
        backtrack(0, [], 0)
        return res


# time complexity 
# O(n * 2^n)
# same as subsetII just add another basecase 