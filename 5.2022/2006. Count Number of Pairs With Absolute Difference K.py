# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in nums:
            for j in nums:
                if i < j and abs(i - j) == k:
                    count += 1
                    
        return count