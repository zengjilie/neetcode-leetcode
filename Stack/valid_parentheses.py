# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if len(stack) != 0 and stack[-1] == '(' and s[i] == ')':
                stack.pop()
            elif len(stack) != 0 and stack[-1] == '{' and s[i] == '}':
                stack.pop()
            elif len(stack) != 0 and stack[-1] == '[' and s[i] == ']':
                stack.pop()
            else:
                stack.append(s[i])
        return not bool(stack)

# time complexity O(n)
# space complexity O(n)

# caveats
# check if the length of stack is 0, 

# summary
# stack functions: append(), pop()
# get the last element use index stack[-1]
# further, above code can be simplified using dict