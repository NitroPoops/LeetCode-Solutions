# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

from math import prod

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mom = [int(i) for i in str(n)]
        
        return prod(mom) - sum(mom)