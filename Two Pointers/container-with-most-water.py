# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1 
        
        while l < r:
            area = (r - l) * min(height[r], height[l])
            res = max(res,area)
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
        return res    
# time complexity O(n)
# space complexity O(1)

