class Solution34:
    def longestEqualZeroOne(self, arr: list[int]) -> int:
        # store first index where each prefix sum was seen
        # initialise with {0: -1} meaning sum=0 exists before index 0
        prefix_map = {0: -1}
        running_sum = 0
        max_len = 0
 
        for i, val in enumerate(arr):
            # treat 0 as -1 so equal 0s and 1s cancel to 0
            running_sum += 1 if val == 1 else -1
 
            if running_sum in prefix_map:
                # same prefix sum seen before → subarray between sums to 0
                length = i - prefix_map[running_sum]
                max_len = max(max_len, length)
            else:
                # only store FIRST occurrence — longer subarray is always better
                prefix_map[running_sum] = i
 
        return max_len