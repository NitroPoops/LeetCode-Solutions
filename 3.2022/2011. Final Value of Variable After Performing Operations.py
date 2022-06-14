# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = 0

        for i in operations:
            if "x" in i:
                n += 1
            else:
                n -= 1

        return n