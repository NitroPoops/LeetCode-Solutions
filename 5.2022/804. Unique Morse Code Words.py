# https://leetcode.com/problems/unique-morse-code-words/

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        
        for word in words:
            temp = []
            for char in word:
                temp.append(morse[ord(char) - ord("a")])
            res.append("".join(temp))
            
        return len(set(res))