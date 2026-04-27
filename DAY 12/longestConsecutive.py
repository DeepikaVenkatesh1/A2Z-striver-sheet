def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
 
        num_set = set(nums)         # O(1) membership check
        max_streak = 0
 
        for num in num_set:
            # only start counting from the beginning of a sequence
            # a sequence start has no predecessor in the set
            if num - 1 not in num_set:
                current = num
                streak = 1
 
                while current + 1 in num_set:
                    current += 1
                    streak += 1
 
                max_streak = max(max_streak, streak)
 
        return max_streak