class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                value = candidates[i]
                
                if value > remaining:
                    continue

                path.append(value)
                dfs(i, path, remaining - value)
                path.pop()

        dfs(0, [], target)
        return res
