from typing import List

"""
Runtime
170 ms

Memory
15.5 MB
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0

        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1

"""
Runtime
614 ms

Memory
15.6 MB
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums.copy()
        
        for num in nums_copy:
            if num == 0:
                nums.pop(nums.index(num))
                nums.append(0)
