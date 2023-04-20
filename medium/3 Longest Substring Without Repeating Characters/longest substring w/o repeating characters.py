"""
Runtime
57 ms

Memory
14.1 MB
"""

# s = "pwwkew"
# s = "bbbbb"
s = "abcabcbb"

def func(s):
    sub = ''
    res = ''
    for i in s:
        if i not in sub:
            sub += i
        else:
            if len(res) <= len(sub):
                res = sub
            sub = sub.split(i)[-1] + i
    return max(len(res), len(sub))

# print(func(s))
