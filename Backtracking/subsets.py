# https://leetcode.com/problems/subsets/submissions/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        
        subset = []
        def dfs(j):
            if j >= len(nums):
                res.append(subset.copy()) 
                return
            
            subset.append(nums[j])
            dfs(j+1)
            
            subset.pop()
            dfs(j+1)
            
        dfs(0)
        return res

# time complexity 
# O(n * 2^n)