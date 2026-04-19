class Solution27:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # prefix_map stores {prefix_sum: how many times it has occurred}
        prefix_map = {0: 1}     # empty subarray has prefix sum 0
        running_sum = 0
        count = 0
 
        for num in nums:
            running_sum += num
 
            # if (running_sum - k) exists in map,
            # those are valid starting points for subarrays ending here
            needed = running_sum - k
            if needed in prefix_map:
                count += prefix_map[needed]
 
            # record current prefix sum in map
            prefix_map[running_sum] = prefix_map.get(running_sum, 0) + 1
 
        return count