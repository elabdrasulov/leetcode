"""
Runtime
8988 ms

Memory
16.8 MB
"""

nums = [2,2,1]

print([num for num in nums if nums.count(num) == 1][0])


"""
Runtime
140 ms

Memory
16.8 MB
"""


nums = [2,2,1]

res = 0

for num in nums:
    res ^= num

print(res)