class Solution32:
    def highestLowestFreqAll(self, arr: list[int]) -> tuple:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
 
        max_count = max(freq.values())
        min_count = min(freq.values())
 
        # collect ALL elements sharing the max/min frequency
        highest = [k for k, v in freq.items() if v == max_count]
        lowest  = [k for k, v in freq.items() if v == min_count]
 
        return sorted(highest), sorted(lowest)