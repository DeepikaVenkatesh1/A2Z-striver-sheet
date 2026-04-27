class Solution40:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water = 0
 
        while left < right:
            if height[left] <= height[right]:
                # left side is the bottleneck
                if height[left] >= max_left:
                    max_left = height[left]     # new max — no water trapped here
                else:
                    water += max_left - height[left]   # water above this bar
                left += 1
            else:
                # right side is the bottleneck
                if height[right] >= max_right:
                    max_right = height[right]   # new max — no water trapped here
                else:
                    water += max_right - height[right]  # water above this bar
                right -= 1
 
        return water