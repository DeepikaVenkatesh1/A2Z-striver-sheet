import math

def smallestDivisor(nums, threshold):
    def can(div):
        return sum(math.ceil(x / div) for x in nums) <= threshold

    low, high = 1, max(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans