nums = [2,7,11,15]
target = 9


dict1 = {}

for i, num in enumerate(nums):
    res = target - nums[i]
    list1 = []

    if res in dict1:
        list1.append(dict1[res])
        list1.append(i)
        print(list1)
        # return list1
    else:
        dict1[num] = i