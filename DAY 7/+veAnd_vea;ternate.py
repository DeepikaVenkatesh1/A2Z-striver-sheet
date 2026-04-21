class Solution20:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        pos_idx = 0   # next available even index for positives
        neg_idx = 1   # next available odd index for negatives
 
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2                    # jump to next even slot
            else:
                result[neg_idx] = num
                neg_idx += 2                    # jump to next odd slot
 
        return result