class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # how to keep relative order while tracking the last 0 pointer?
        slow = fast = 0
        n = len(nums)

        for fast in range(n):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
