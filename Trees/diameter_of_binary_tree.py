# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global max_di
        max_di = 0

        def dfs(root):
            # nonlocal max_di

            if not root:
                return -1
            else:
                lh = dfs(root.left)
                rh = dfs(root.right)
                mh = max(lh + 1, rh + 1)
                cur_di = lh + rh + 2
                max_di = max(max_di, cur_di)
                return mh

        dfs(root)

        return max_di


# time complexity O(n)
# space complexity O(1)