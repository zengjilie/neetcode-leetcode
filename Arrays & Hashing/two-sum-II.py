# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l]+numbers[r] > target:
                r -= 1
            if numbers[l]+numbers[r] < target:
                l += 1
        return [l+1, r+1]

# time complexity O(n^2)
# space complexity O(1)

# two pointers
