"""
Runtime
151 ms

Memory
18.1 MB
"""

intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
intervals.sort(key=lambda x:x[0])
res = []

for i in intervals:
    if not res or res[-1][-1]<i[0]:
        res.append(i)
    else:
        res[-1][-1] = max(res[-1][-1], i[-1])

print(res)