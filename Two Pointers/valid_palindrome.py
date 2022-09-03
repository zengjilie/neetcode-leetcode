# https://leetcode.com/problems/valid-palindrome/

# time complexity O(n)
# space complexity O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))

        ans = True

        for i in range(0, len(s)):
            pa = i
            va = s[pa]
            pb = len(s) - 1 - i
            vb = s[pb]

            if (pa == pb or pa > pb):
                return ans

            if (va != vb):
                ans = False

        return ans


# =======

# time complexity O(n)
# space complexity O(1)

# edge case:
# '.,'
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pl, pr = 0, len(s) - 1
        
        while pl != pr and pl < pr:
            while pl < pr and not self.alphanum(s[pl]): # this pl < pr is easy to forget
                pl += 1
            while pl < pr and not self.alphanum(s[pr]): 
                pr -= 1
            if(s[pl].lower() != s[pr].lower()):
                return False
            pl += 1
            pr -= 1
        return True
        
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
