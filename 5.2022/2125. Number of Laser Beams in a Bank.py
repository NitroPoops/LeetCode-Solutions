# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = []
        
        for i in bank:
            if "1" in i:
                n.append(i.count("1"))

        return sum(n[i] * n[i + 1] for i in range(len(n) - 1))