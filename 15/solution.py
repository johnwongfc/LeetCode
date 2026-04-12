class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum < 0:
                    l += 1
                elif _sum > 0:
                    r -= 1
                else:
                    triplets.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return triplets
