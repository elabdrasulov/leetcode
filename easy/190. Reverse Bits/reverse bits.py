
"""
Runtime
32 ms

Memory
13.8 MB
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = bin(n)[2:][::-1]+("0"*(32-len(bin(n)[2:])))
        return int(res,2)