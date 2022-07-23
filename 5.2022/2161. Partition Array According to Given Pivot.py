# https://leetcode.com/problems/partition-array-according-to-given-pivot/

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        equal = []

        for i in nums:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                big.append(i)
            else:
                equal.append(i)
                
        return small + equal + big