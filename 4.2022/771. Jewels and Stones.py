# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        
        for s in range(len(stones)):
            for j in range(len(jewels)):
                if stones[s] == jewels[j]:
                    count += 1
                    
        return count