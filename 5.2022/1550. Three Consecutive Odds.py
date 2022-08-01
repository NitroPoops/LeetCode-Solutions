# https://leetcode.com/problems/three-consecutive-odds/

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        one, two, three = 0, 1, 2
        while three < len(arr):
            if arr[one] % 2 != 0 and arr[two] % 2 != 0 and arr[three] % 2 != 0:
                return True
            one += 1
            two += 1
            three += 1