class Solution21:
    def nextPermutation(self, nums: list[int]) -> None:
    
        n = len(nums)
        i = n - 2
 
        # Step 1: find break point from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
 
        if i >= 0:
            # Step 2: find rightmost element greater than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # swap
 
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1