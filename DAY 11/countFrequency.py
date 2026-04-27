class Solution:
    def countFrequency(self,arr:list)->dict:
        freq={}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1
 
        return freq
 
    def highestLowestFreq(self, arr: list[int]) -> tuple:
        freq = self.countFrequency(arr)
 
        max_count = max(freq.values())
        min_count = min(freq.values())
 
        max_elem = [k for k, v in freq.items() if v == max_count][0]
        min_elem = [k for k, v in freq.items() if v == min_count][0]
 
        return max_elem, min_elem

