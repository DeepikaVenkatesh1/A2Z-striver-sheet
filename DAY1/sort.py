class Solution:
    def isSorted(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:   # found a drop → not sorted
                return False
        return True  