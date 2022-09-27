# https://leetcode.com/problems/last-stone-weight/
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)   
        
        while len(stones) > 1 :
            y = heapq.heappop(stones)  
            x = heapq.heappop(stones)
            if x != y:
                new_value = y - x
                heapq.heappush(stones, new_value) 
                
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])

# time complexity 
# O(logn)