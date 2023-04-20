"""
Runtime
2130 ms

Memory
25.4 MB
"""

nums = [1,2,3,4,5,6,7]
k = 3

for i in range(k):
    nums.insert(0, nums[-1])
    nums.pop()



"""
Runtime
197 ms

Memory
26 MB
"""

temp = []
k = k % len(nums)
temp.extend(nums[len(nums)-k:])
temp.extend(nums[:len(nums)-k])
nums.clear()
nums.extend(temp)