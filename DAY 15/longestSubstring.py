def length_of_longest_substring(s):
    char_index = {}  # char → most recent index
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        # If char seen AND it's inside current window → shrink left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right  # update last seen
        max_len = max(max_len, right - left + 1)

    return max_len