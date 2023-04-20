from typing import List

"""
Runtime
173 ms

Memory
15.6 MB
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = nums[0]
        i = 0
        
        while i<len(nums)-1:
            if num == nums[i+1]:
                nums.remove(nums[i+1])
            else:
                num = nums[i+1]
                i+=1
        return len(nums)