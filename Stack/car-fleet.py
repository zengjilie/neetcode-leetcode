# https://leetcode.com/problems/car-fleet/
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = [] 
        
        for p,s in sorted(pair)[::-1]:
            t = (target-p)/s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)

# time complexity O(n * logn)
# space complexity O(n)

