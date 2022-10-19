# https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        
        while l<r:
            if maxL <= maxR:
                l+=1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            if maxL > maxR:
                r-=1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res

# time complexity O(n)
# space complexity O(1)
