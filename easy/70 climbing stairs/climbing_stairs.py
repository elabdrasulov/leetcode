"""
Runtime
31 ms

Memory
13.8 MB
"""

n = 5
def func(n):
    if n == 1:
        return 1

    n1 = 1
    n2 = 2

    for i in range(3, n+1):
        n1,n2 = n2, n1+n2

    return n2
print(func(n))



# def climbStairs(n: int) -> int:
#     if n <= 2:
#         return n
#     dp = [0]*n
#     dp[0], dp[1] = 1, 2
#     for i in range(2, n):
#         dp[i] = dp[i-1] + dp[i-2]
#     print(dp)
#     return dp[-1]

# print(climbStairs(n))