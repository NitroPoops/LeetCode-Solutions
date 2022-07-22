# https://leetcode.com/problems/rearrange-array-elements-by-sign/

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        positive = []
        negative = []

        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)

        for x, y in zip(positive, negative):
            res += [x, y]
            
        return res