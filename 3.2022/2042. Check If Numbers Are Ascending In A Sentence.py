# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        r = [int(i) for i in s.split() if i.isdigit()]
        
        return r == sorted(list(set(r)))