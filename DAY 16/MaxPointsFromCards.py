class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k        # size of middle portion to MINIMIZE

        # Edge case: take all cards
        if window_size == 0:
            return sum(cardPoints)

        # Build first window (leftmost n-k elements)
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum
        total = sum(cardPoints)

        # Slide window across the array
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, window_sum)

        return total - min_window
