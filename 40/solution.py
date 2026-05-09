class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[::])
                return

            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break

                # all duplicates are next to each other
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(value)
                backtrack(i + 1, path, remaining - value)
                path.pop()

        backtrack(0, [], target)
        return result