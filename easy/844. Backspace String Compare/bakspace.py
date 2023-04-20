"""
Runtime
31 ms

Memory
13.9 MB
"""

s = "ab#c"
t = "ad#c"

def func(s):
    res = []
    for i in s:
        if i !='#':
            res.append(i)
        elif res:
            res.pop()

    return "".join(res)

print(func(s) == func(t))