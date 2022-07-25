# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        
        result = [words[i] for i in range(k)]
        
        return " ".join(result)