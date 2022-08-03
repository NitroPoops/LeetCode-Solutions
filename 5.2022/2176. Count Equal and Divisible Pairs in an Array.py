# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0 <= i < j < len(nums) and nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
                    
        return count