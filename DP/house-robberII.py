# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case [1]

        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

# time complexity O(n)
# space complexity O(1)

# [2,3,2]
# rob1
# [2,3], peel off the last one
# not rob1
# [3,2], not neet to peel off
