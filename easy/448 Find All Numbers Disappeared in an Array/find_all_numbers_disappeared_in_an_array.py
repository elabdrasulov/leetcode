"""
Runtime
415 ms

Memory
22.2 MB
"""


nums = [4,3,2,7,8,2,3,1]
i = 0

while i<len(nums):
    pos = nums[i] - 1
    if nums[i]!=nums[pos]:
        nums[i], nums[pos] = nums[pos], nums[i]
    else:
        i+=1
# print(nums)

# res = []

# for i in range(len(nums)):
#     if nums[i] != i+1:
#         res.append(i+1)
res = [i+1 for i in range(len(nums)) if nums[i]!= i+1]
print(res)


"""
Runtime
375 ms

Memory
26.3 MB
"""

nums = [4,3,2,7,8,2,3,1]

print(list(set(i for i in range(1,len(nums)+1)) - set(nums)))