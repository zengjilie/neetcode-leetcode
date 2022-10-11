# https://leetcode.com/problems/reformat-the-string/
class Solution:
    def reformat(self, s: str) -> str:
        if not s:
            return ""
        
        x = []
        y = []
        for i in s:
            if i.isalpha():
                x.append(i)
            if i.isnumeric():
                y.append(i)
        if abs(len(x) - len(y)) > 1:
            return ""
        else: 
            if len(x) < len(y):
                temp = x
                x = y
                y = temp
                
            ans=""
            i = 0
            
            while i < len(x) and i < len(y):
                ans += x[i]
                ans += y[i]
                i+=1
                
            if len(x) != len(y):
                ans += x[i]
            
            return ans

# caveat:
# add the longer list first
# [1,2,3] ['a','b']
# add numbers first