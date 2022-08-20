# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lengths = [min(r) for r in rectangles]

        return lengths.count(max(lengths))