from typing import List

"""
Runtime
1738 ms

Memory
16.2 MB
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sett = set(nums)
        for i in sett.copy():
            if i in nums and nums.count(i)>1:
                sett.remove(i)
        return list(sett)[0]



"""
Runtime
3816 ms

Memory
15.9 MB
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = {i:nums.count(i) for i in nums}

        for k,v in l.items():
            if v == 1:
                return k

"""
Runtime
56 ms

Memory
16.1 MB
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}

        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1

        for k,v in dict1.items():
            if v == 1:
                return k