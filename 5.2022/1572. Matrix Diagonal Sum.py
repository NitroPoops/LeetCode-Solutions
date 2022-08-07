# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left = 0
        right = len(mat) - 1
        length = len(mat)
        res = 0
        
        for rowIndex in range(length):
            res += mat[rowIndex][left]
            left += 1
            res += mat[rowIndex][right]
            right -= 1
            
        if len(mat) % 2 != 0:
            res -= mat[length//2][length//2]
            
        return res