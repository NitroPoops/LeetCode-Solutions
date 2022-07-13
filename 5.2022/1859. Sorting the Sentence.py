# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        n = []
        word = []

        s = s.split()
        for w in s:
            n.append(w[-1])
            word.append(w[:-1])
            
        res = []
        for _, a in sorted(list(zip(n, word))):
            res.append(a)
            
        return " ".join(res)