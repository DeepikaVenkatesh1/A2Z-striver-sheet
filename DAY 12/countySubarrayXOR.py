class Solution35:
    def countSubarraysXOR(self, arr: list[int], k: int) -> int:
        xor_map = {0: 1}        # XOR value 0 seen once before array starts
        curr_xor = 0
        count = 0
 
        for val in arr:
            curr_xor ^= val     # running XOR with current element
 
            # how many previous prefix XORs satisfy: prev == curr_xor ^ k
            needed = curr_xor ^ k
            if needed in xor_map:
                count += xor_map[needed]
 
            # record current prefix XOR
            xor_map[curr_xor] = xor_map.get(curr_xor, 0) + 1
 
        return count