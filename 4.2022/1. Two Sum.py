# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []

        for idx in range(len(nums)):
            for i in range(len(nums)):
                if idx != i and nums[idx] + nums[i] == target:
                        r.append(idx)

        return r