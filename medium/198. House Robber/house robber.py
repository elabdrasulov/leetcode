from typing import List

"""
Runtime
36 ms

Memory
13.8 MB
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        nums = [0]*3+nums

        for i in range(3, len(nums)):
            house1 = nums[i-3]+nums[i]
            house2 = nums[i-2]+nums[i]
            nums[i] = max(house1, house2)

        profit = max(nums)
        
        return profit
