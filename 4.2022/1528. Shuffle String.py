# https://leetcode.com/problems/shuffle-string/

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [v for _, v in sorted(zip(indices, s))]

        return "".join(res)