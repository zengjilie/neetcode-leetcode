# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        ans = []

        for i, val in enumerate(nums):
            if ((target - val) in hash_map):
                ans.append(hash_map.get(target-val))
                ans.append(i)
            else:
                hash_map[val] = i

        return ans
