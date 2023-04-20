from typing import List

"""
Runtime
31 ms

Memory
13.8 MB
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1