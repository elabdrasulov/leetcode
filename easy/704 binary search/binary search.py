"""
Runtime
250 ms

Memory
15.4 MB
"""

nums = [-1,0,3,5,9,12]
target = 9

# from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1
        

# left = 0
# right = len(nums)-1

# while left<=right:
#     mid = (left+right)//2
#     if nums[mid]>target:
#         right = mid - 1
#     elif nums[mid]<target:
#         left = mid + 1
#     else:
#         print(mid)
#         break
# return -1

"""
Runtime
32 ms

Memory
15.7 MB
"""

from bisect import bisect_left
from sys import stdin

f = open("user.out", 'w')
for nums, tar in zip(stdin, stdin):
    tar = int(tar.rstrip())
    a = nums.rstrip()[1:-1].split(',')
    i = bisect_left(a, True, key=lambda x: int(x) >= tar)
    print(i if i < len(a) and int(a[i]) == tar else -1, file=f)
exit()


    