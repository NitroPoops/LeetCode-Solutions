# https://leetcode.com/problems/count-the-number-of-consistent-strings/

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            temp = 0
            for char in word:
                if char in allowed:
                    temp += 1
            if len(word) == temp:
                count += 1
        
        return count