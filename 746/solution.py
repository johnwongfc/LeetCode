class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dp(i):
            # base Case
            if i >= n:
                return 0

            if i in cache:
                return cache[i]
            
            one_step = dp(i + 1)
            two_step = dp(i + 2)

            # recursive case
            cache[i] = cost[i] + min(one_step, two_step)
            return cache[i]


        cache = {}
        return min(dp(0), dp(1))
