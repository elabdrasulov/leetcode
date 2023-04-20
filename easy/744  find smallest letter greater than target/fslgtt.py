"""
Runtime
120 ms

Memory
14.3 MB
"""


letters = ["c","f","j"]
target = "a"

def func(letters, target):
    for i in letters:
        if i > target:
            return i
    return letters[0]

print(func(letters, target))


"""
Runtime
109 ms

Memory
14.2 MB
"""


left = 0
right = len(letters)


while left<right:
    # mid = left+right//2
    mid = left+(right-left)//2
    if letters[mid]<=target:
        left = mid + 1
    else:
        right = mid

print(letters[left%len(letters)])
