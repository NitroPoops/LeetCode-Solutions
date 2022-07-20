# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import List
from math import sqrt

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []

        for j in queries:
            temp = 0
            for i in points:
                if sqrt((j[0]-i[0]) ** 2 + (j[1]-i[1]) ** 2) <= j[2]:
                    temp += 1
            res.append(temp)
                    
        return res