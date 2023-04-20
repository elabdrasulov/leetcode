"""
Runtime
130 ms

Memory
15.2 MB
"""

nums = [9,6,4,2,3,5,7,0,1]

n = len(nums)

print((n*(n+1)//2)-sum(nums))