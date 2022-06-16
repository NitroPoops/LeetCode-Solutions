# https://leetcode.com/problems/number-of-good-pairs/

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        r = []
        
        for f in range(len(nums)):
            for s in range(len(nums)):
                if f < s and nums[f] == nums[s]:
                    r.append((f, s))
                    
        return len(r)