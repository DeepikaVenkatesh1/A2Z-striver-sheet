class Solution:
    def secondLargest(self, arr: list[int]) -> int:
        largest = float('-inf')
        second = float('-inf')

        for num in arr:
            if num > largest:
                second = largest      # old largest becomes second
                largest = num         # update largest
            elif num > second and num != largest:
                second = num          # update second only

        return second if second != float('-inf') else -1