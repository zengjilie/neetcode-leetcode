# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
            
        return min(cost[0], cost[1])


# time complexity O(n)
# space complexity O(1)

# similar to the climb-stairs problem
