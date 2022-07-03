# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = str(nums[i+1])
            r.extend(freq * [val])

        return r