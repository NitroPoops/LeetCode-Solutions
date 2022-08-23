# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        things = piles[len(piles) // 3:]

        return sum(things[::2])