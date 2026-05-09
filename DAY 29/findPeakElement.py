class Solution75:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        rows, cols = len(mat), len(mat[0])
        low, high  = 0, cols - 1
 
        while low <= high:
            mid_col = low + (high - low) // 2
 
            # find row with max value in this column
            max_row = 0
            for r in range(rows):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r
 
            left  = mat[max_row][mid_col - 1] if mid_col > 0        else -1
            right = mat[max_row][mid_col + 1] if mid_col < cols - 1 else -1
 
            if mat[max_row][mid_col] > left and mat[max_row][mid_col] > right:
                return [max_row, mid_col]       # peak found
            elif left > mat[max_row][mid_col]:
                high = mid_col - 1              # peak is in left half
            else:
                low  = mid_col + 1              # peak is in right half
 
        return [-1, -1]