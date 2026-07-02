# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root):
        if not root:
            return []
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                return 0

            curr_level = max(dfs(node.left), dfs(node.right)) + 1

            if curr_level > len(res):   
                res.append([])

            res[curr_level - 1].append(node.val)
            return curr_level
        dfs(root)
        return res
