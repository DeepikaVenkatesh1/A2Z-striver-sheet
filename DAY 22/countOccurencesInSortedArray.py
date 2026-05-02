class Solution57:
    def countOccurrences(self, nums: list[int], target: int) -> int:
        first = self._firstOccurrence(nums, target)
        if first == -1:
            return 0
        last = self._lastOccurrence(nums, target)
        return last - first + 1
 
    def _firstOccurrence(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans
 
    def _lastOccurrence(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                ans = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return ans