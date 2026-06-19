from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        counts = Counter(tiles)

        def dfs():
            nonlocal res

            for letter in counts:
                if counts[letter] > 0:
                    counts[letter] -= 1
                    res += 1
                    dfs()
                    counts[letter] += 1

        dfs()
        return res