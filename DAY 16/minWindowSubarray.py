from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)       
        have = {}               
        formed = 0              
        required = len(need)    
        left = 0
        min_len = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            # Check if this char's count just met the requirement
            if char in need and have[char] == need[char]:
                formed += 1

            # Try to shrink window while all chars are satisfied
            while formed == required:
                # Update result if this window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Shrink from left
                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return result