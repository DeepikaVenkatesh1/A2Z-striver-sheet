class Solution10:
    def intersect_sorted_arrays(self, arr1: list[int], arr2: list[int]) -> list[int]:
        result = []
        i, j = 0, 0                          # two pointers, one for each array
 
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                # avoid duplicates in result
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1                       # arr1 is behind, advance it
            else:
                j += 1                       # arr2 is behind, advance it
 
        return result