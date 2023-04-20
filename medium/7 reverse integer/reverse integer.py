from typing import List

"""
Runtime
34 ms

Memory
13.8 MB
"""

class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if res.bit_length()<32:
            if x>0: 
                return res
            else: 
                return -res
        return 0