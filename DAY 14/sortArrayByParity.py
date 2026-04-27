class Solution42:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
 
        while left < right:
            # advance left until we hit an odd number
            while left < right and nums[left] % 2 == 0:
                left += 1
            # advance right until we hit an even number
            while left < right and nums[right] % 2 == 1:
                right -= 1
 
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
 
        return nums