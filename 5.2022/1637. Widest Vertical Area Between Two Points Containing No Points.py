# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(c[0] for c in points)
        width = 0

        for i in range(len(x) - 1):
            temp = abs(x[i] - x[i+1])
            if temp > width:
                width = temp

        return width