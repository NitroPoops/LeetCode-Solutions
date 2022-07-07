# https://leetcode.com/problems/sort-array-by-parity/

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        
        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        return evens + odds