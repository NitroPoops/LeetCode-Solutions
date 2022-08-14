# https://leetcode.com/problems/find-the-highest-altitude/

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        highest = 0
        
        for i in gain:
            highest += i
            if highest > res:
                res = highest
                
        return res