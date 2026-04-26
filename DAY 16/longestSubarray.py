class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeros = 0       # count of zeros in current window
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            # Window invalid: more than 1 zero → shrink
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # -1 because we must delete exactly one element
            max_len = max(max_len, right - left + 1 - 1)

        return max_len