# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = s.split()
        n = 0
        
        for i in l:
            if i.isdigit():
                if int(i) <= n:
                    return False
                n = int(i)
                
        return True