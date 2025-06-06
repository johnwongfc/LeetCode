# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS, append last item of each level to res
        Time: o(n)
        """
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == size - 1:
                    res.append(node.val)

        return res
