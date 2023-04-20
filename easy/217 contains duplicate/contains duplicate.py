"""
Runtime
1069 ms

nums = [1,1,1,3,3,4,3,2,4,2]

nums.sort()
for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        return True
return False

"""


"""
Runtime
473 ms

nums = [1,1,1,3,3,4,3,2,4,2]

len(nums) != len(set(nums))
"""

"""
Runtime
577 ms

nums = [1,1,1,3,3,4,3,2,4,2]

def func(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
"""

nums = [1,1,1,3,3,4,3,2,4,2]

seen = set()

for num in nums:
    if num in seen:
        print(True)
    seen.add(num)

print(seen)



