class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        _max = 0

        while l < r:
            width = r - l
            curr_area = min(height[l], height[r]) * width

            _max = max(_max, curr_area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return _max
