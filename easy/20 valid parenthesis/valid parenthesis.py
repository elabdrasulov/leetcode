"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

"""

"""
Runtime
29 ms

Memory
13.8 MB
"""


# s = '()[]{}'
# s = '{}'
s = '[]{}()'

def func(s):
    par = {
        '(':')',
        '[':']',
        '{':'}'
    }

    res = []

    for c in s:
        if c in par:
            res.append(c)
        else:
            if (len(res) and par[res[-1]]) == c:
                del res[-1]
            else:
                return False
    return res == []
    

# def isValid(s):
#     while '()' in s or '[]' in s or '{}' in s:
#         s = s.replace('()', '').replace('[]', '').replace('{}', '')
#         return s == ''

# print(func(s))




# nums = [2,5,3,4]
# target = 6

# hm = {}

# for i, num in enumerate(nums):
#     if target-num in hm:
#         return [hm[target-num], i]
#     else:
#         hm[num] = i
