# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        i = 1
        while n != 0:
            mod = n%2
            ans += mod
            n = n>>1
        return ans
        