class Solution54:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = len(nums)             # default: insert at end
 
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                ans = mid           # could be the insert position — check left
                high = mid - 1
            else:
                low = mid + 1
 
        return ans