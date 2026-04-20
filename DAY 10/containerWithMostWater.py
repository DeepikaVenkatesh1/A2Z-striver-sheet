class Solution30:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
 
        while left < right:
            # water trapped = min height × width
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)
 
            # move the shorter wall inward — keeping the taller one
            # gives the only chance of finding a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
 
        return max_water