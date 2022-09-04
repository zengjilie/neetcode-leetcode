# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        return self.recurse(nums, l, r, target)

    def recurse(self, nums, l, r, target):
        mid = round((r+l)/2)

        if r == l and target != nums[mid]:
            return -1

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            if mid+1 <= r:  # this part is esay to forget, dealing with caveats
                return self.recurse(nums, mid+1, r, target)
            else:
                return -1
        elif target < nums[mid]:
            if l <= mid - 1:
                return self.recurse(nums, l, mid-1, target)
            else:
                return -1

        return

# time complexity O(logn)
# space complexity O(1)

# caveats
# [2,5] 0, target will less then the smallest value, vice versa
# [2,5] 2, target will equal to the smallest value, vice versa


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = round(l + r)
            if target > nums[mid]:
                l = mid + 1
                r = r
            elif target < nums[mid]:
                l = l
                r = mid - 1
            else:
                return mid
        return -1


# summary
# use while loop please, its way faster
