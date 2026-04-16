class Solution18:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
 
        for num in nums[1:]:
            # extend current subarray OR start fresh from current element
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
 
        return max_sum