# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while (l in range(len(s)) and
                   r in range(len(s)) and
                   s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while (l in range(len(s)) and
                   r in range(len(s)) and
                   s[l] == s[r]):
                res += 1
                l -= 1
                r += 1

        return res

# time complexity O(n)
# space complexity O(1)

# same as longest-palindromic-substring
