# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sorting can possibly achieve better time complexity
        nums.sort()
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)

        return False
