from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n

        # left to right
        for i in range(1, n):
            prev = ratings[i - 1]
            curr = ratings[i]

            if curr > prev:
                res[i] = res[i - 1] + 1

        # right to left
        for i in range(n - 2, -1, -1):
            left = ratings[i]
            right = ratings[i + 1]
            if left > right:
                res[i] = max(res[i + 1] + 1, res[i])

        return sum(res)
 
