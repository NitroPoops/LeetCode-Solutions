# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:idx + 1]) for idx in range(len(nums))]
