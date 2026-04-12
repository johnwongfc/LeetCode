class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        valid_count = 0

        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1

            while l < r:
                a, b, c = nums[l], nums[r], nums[i]
                if a + b > c:
                    valid_count += (r - l)
                    r -= 1
                else:
                    l += 1

        return valid_count
