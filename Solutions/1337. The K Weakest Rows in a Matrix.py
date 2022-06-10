# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        L = [(sum(a), i) for i, a in enumerate(mat)]
        
        return [x[1] for x in sorted(L)[:k]]
