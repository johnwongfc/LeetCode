class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
        base case:
        recursive case:
        cache
        """
        m = len(triangle)

        def dp(r, c):
            if r == m - 1:
                return triangle[r][c]
            # check for bound
            if c == r + 1:
                return float("inf")

            if (r, c) in cache:
                return cache[(r, c)]

            down = dp(r + 1, c)
            down_right = dp(r + 1, c + 1)
            cache[(r, c)] = triangle[r][c] + min(down, down_right)
            return cache[(r, c)]

        cache = {}
        return dp(0, 0)
