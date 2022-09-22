# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if root:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 
            else:
                return 0


# time complexity O(n)
# space complexity O(1)