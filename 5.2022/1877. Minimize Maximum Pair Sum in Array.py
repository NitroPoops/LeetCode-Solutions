# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        pairs = []
        
        while left < right:
            pairs.append(nums[left] + nums[right])
            
            left += 1
            right -= 1
            
        return max(pairs)