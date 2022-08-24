# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        left = 0
        right = len(s) - 1
        
        countLeft = 0
        countRight = 0
        
        while left < right:
            if s[left] in vowels:
                countLeft += 1
            if s[right] in vowels:
                countRight += 1
            
            left += 1
            right -= 1
            
        return countLeft == countRight