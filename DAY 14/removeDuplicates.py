class Solution41:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0   # write pointer — where to place the next valid element
 
        for num in nums:
            # first two positions are always valid
            # beyond that: only write if current != element two slots back
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
 
        return i 