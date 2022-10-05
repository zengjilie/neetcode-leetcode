# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[amount] = 0

        for i in range(amount, -1, -1):
            for c in coins:
                if i+c in range(amount+1):
                    dp[i] = min(dp[i], 1+dp[i+c])

        return dp[0] if dp[0] != amount+1 else -1

# time complexity O(amount*len(list))
# space complexity O(amount)
