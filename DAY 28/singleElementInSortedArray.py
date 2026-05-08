class Solution71:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            # ensure mid is even so we check (mid, mid+1) pairs
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # pair is intact — single element is to the right
                low = mid + 2
            else:
                # pair broken — single element is at mid or to the left
                high = mid

        return nums[low]


