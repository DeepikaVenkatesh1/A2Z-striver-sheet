class Solution52:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
 
        while low <= high:
            mid = low + (high - low) // 2   # safe midpoint — no overflow
 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1               # target is in right half
            else:
                high = mid - 1              # target is in left half
 
        return -1