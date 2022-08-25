# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num = nums.copy()
        
        for i in range(1, len(num)):
            num[i] = max(num[i-1] + 1, num[i])
            # replace current number with the previous number + 1, or keep the current number (because it is already bigger than the previous number)
            
        return sum(num) - sum(nums)