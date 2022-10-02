# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            # odd
            l, r = i, i
            while r in range(len(s)) and l in range(len(s)) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                r += 1
                l -= 1
            # even
            l, r = i, i+1

            while r in range(len(s)) and l in range(len(s)) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                r += 1
                l -= 1
        return res

# time complexity O(n^2)
# space complexity O(1)