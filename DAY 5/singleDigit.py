class Solution:
    def singleDigit(self,nums:list)->int:
        result = 0
        for num in nums:
            result=result^num
        return result
sol = Solution()
print(sol.singleDigit([1,1,2,4,5,4,2,5,6]))