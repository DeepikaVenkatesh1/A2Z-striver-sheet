class Solution12:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current = 0
 
        for num in nums:
            if num == 1:
                current += 1                 # extend current streak
                max_count = max(max_count, current)
            else:
                current = 0                  # reset on seeing 0
 
        return max_count