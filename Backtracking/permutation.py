# https://leetcode.com/problems/permutations/ 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permute(nums)
             
            for perm in perms:
                perm.append(n)
                
            result.extend(perms)
            nums.append(n)
            
        return result


# time complexity 
# O(n * (n-1) * (n-2) .. 1) = O(n!) 