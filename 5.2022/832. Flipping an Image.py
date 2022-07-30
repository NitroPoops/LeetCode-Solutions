# https://leetcode.com/problems/flipping-an-image/

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for numIndex in range(len(row)):
                if row[numIndex] == 1:
                    row[numIndex] = 0
                else:
                    row[numIndex] = 1
                    
        return image