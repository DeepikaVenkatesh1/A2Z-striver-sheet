 
class Solution23:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
 
        num_set = set(nums)
        max_streak = 0
 
        for num in num_set:
            # only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1
 
                # extend the sequence as far as possible
                while current + 1 in num_set:
                    current += 1
                    streak += 1
 
                max_streak = max(max_streak, streak)
 
        return max_streak