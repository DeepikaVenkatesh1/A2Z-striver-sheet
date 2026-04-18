class Solution22:
    def leaders(self, arr: list[int]) -> list[int]:
        result = []
        max_from_right = float('-inf')
 
        # scan right to left
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_from_right:
                result.append(arr[i])               # current is a leader
                max_from_right = arr[i]             # update running max
 
        result.reverse()                            # restore left-to-right order
        return result