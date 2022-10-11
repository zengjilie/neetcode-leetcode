# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
def solution(nums):
    if len(nums) == 1:
        return 0
    ans = 0
    i, j = 0, 1
    while j < len(nums):
        if nums[i] <= nums[j]:
            ans = max(ans, nums[j] - nums[i])
        else:
            i = j
        j+=1
    return ans

nums = [7, 9, 5, 6, 3, 2]
print(solution(nums))