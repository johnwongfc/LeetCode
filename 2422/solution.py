class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Initialize two pointers: left at the start and right at the end of the array
        Track leftSum and rightSum starting with the values at those positions
        While left < right:
            If leftSum equals rightSum, both ends match; 
                move both pointers inward and reset their sums to the new positions
            If leftSum < rightSum, the left side needs more artifacts; 
                merge by incrementing left pointer and adding that value to leftSum, counting one operation
            If rightSum < leftSum, the right side needs more artifacts; 
                merge by decrementing right pointer and adding that value to rightSum, counting one operation
        Return the total operation count
        """
        
        left, right = 0, len(nums) - 1
        left_sum, right_sum = nums[left], nums[right]
        operations = 0

        while left < right:
            if left_sum == right_sum:
                left += 1
                right -= 1
                if left < right:
                    left_sum = nums[left]
                    right_sum = nums[right]
            elif left_sum < right_sum:
                left += 1
                left_sum += nums[left]
                operations += 1
            elif left_sum > right_sum:
                right -= 1
                right_sum += nums[right]
                operations += 1
        return operations
