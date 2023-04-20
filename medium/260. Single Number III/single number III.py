from typing import List

"""
Runtime
3221 ms

Memory
16.7 MB
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sett = set(nums)
        for i in sett.copy():
            if i in nums and nums.count(i)>1:
                sett.remove(i)
        return list(sett)
    

nums = [1,2,1,3,2,5]
# Output: [3,5]

"""
Runtime
65 ms

Memory
16.2 MB
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hm = {}
        res = []

        for num in nums:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1

        for k,v in hm.items():
            if v == 1:
                res.append(k)

        return res
