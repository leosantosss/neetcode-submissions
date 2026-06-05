class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top  = 0
        bottom  = len(matrix) - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix [mid_row][0]:
                bottom = mid_row - 1
            else:
                break
        
        if not (top <= bottom):
            return False

        l = 0
        r = len(matrix[mid_row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True
        return False
