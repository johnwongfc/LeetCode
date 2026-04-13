class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lo, hi = 0, n - 1
        i = 0
        while i <= hi:
            if nums[i] == 0:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[hi], nums[i] = nums[i], nums[hi]
                hi -= 1
