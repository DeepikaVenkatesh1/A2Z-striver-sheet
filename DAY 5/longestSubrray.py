class Solution:
    def longestSubarrayWithSumK(self, arr: list[int], k: int) -> int:
        left = 0
        window_sum = 0
        max_len = 0

        for right in range(len(arr)):
            window_sum += arr[right]             # expand window to the right

            while window_sum > k and left <= right:
                window_sum -= arr[left]          # shrink from the left
                left += 1

            if window_sum == k:
                max_len = max(max_len, right - left + 1)

        return max_len
    
sol = Solution()
print(sol.longestSubarrayWithSumK([1, 2, 3, 4, 5], 9))
