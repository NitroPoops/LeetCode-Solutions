# https://leetcode.com/problems/minimum-time-visiting-all-points/

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        
        for i in range(len(points) - 1):
            count += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
        
        return count