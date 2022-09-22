# https://leetcode.com/problems/balanced-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        
        def dfs(root):
            nonlocal is_balanced
            
            if not root:
                return 0
            else:
                lh = dfs(root.left)  
                rh = dfs(root.right)
                if abs(lh - rh) > 1:
                    is_balanced = False
                return max(lh, rh) + 1
            
        dfs(root)
        
        return is_balanced


# time complexity O(n)
# space complexity O(1)

# same stuff, find the height, dfs traversal