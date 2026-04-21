class Solution24:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
 
        Key insight:
          - matrix[i][0] = 0 means row i should be zeroed
          - matrix[0][j] = 0 means col j should be zeroed
          - matrix[0][0] is shared → use separate flag 'col0'
            to track whether the first column itself needs zeroing
        """
        rows = len(matrix)
        cols = len(matrix[0])
        col0 = False                                # flag for first column
 
        # Step 1: mark first row and first column as flags
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = True                         # first col needs zeroing
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0               # mark row
                    matrix[0][j] = 0               # mark col
 
        # Step 2: zero inner cells based on markers (bottom-right → top-left)
        # go in reverse so we don't overwrite markers before using them
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
 
        # Step 3: zero first column if flagged
        if col0:
            for i in range(rows):
                matrix[i][0] = 0