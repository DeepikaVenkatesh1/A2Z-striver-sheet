class Solution:
    def spiralMatrix(self,matrix:list[list[int]])->list[int]:
        result=[]
        if not matrix:
            return result
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        while left<=right and top<=bottom:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
 
            # Move down along right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
 
            # Move left along bottom row (only if rows remain)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
 
            # Move up along left column (only if columns remain)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
 
        return result




