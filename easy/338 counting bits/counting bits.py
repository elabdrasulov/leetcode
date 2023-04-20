"""
Runtime
283 ms

Memory
20.9 MB
"""

n = 5

res = []

for i in range(n+1):
    if i == 0:
        num = 0
    else:
        num = int(str(bin(i))[2:])
    res.append(sum(list(map(int, str(num)))))

print(res)

