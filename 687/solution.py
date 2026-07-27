# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0

        if not root:
            return 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_contrib, right_contrib = 0, 0

            if node.left and node.left.val == node.val:
                left_contrib = left + 1
            if node.right and node.right.val == node.val:
                right_contrib = right + 1

            res = max(res, left_contrib + right_contrib)
            return max(left_contrib, right_contrib)

        dfs(root)
        return res