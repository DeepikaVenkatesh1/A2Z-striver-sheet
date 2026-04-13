class Solution:
    def unionSortedArrays(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i, j = 0, 0
        result = []

        while i < len(arr1) and j < len(arr2):
            if i > 0 and arr1[i] == arr1[i - 1]:
                i += 1
                continue
            if arr1[i] <= arr2[j]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
            else:
                if not result or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1

        while i < len(arr1):
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1

        while j < len(arr2):
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

        return result
sol=Solution()
print(sol.unionSortedArrays([1,2,3,4,5],[3,4,5,8,9]))