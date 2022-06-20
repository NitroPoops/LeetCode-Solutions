# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        r = []
        
        for idx in range(len(candies)):
            if candies[idx] + extraCandies >= max(candies):
                r.append(True)
            else:
                r.append(False)
                
        return r