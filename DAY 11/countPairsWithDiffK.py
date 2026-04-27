class Solution33:
    def countPairsWithDiffK(self, arr: list[int], k: int) -> int:
        if k < 0:
            return 0
 
        num_set = set(arr)          # O(1) lookup
        count = 0
 
        for num in num_set:         # iterate over SET to avoid duplicate pairs
            if num + k in num_set:
                count += 1
 
        return count
