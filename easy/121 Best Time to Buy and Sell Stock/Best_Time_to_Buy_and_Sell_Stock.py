"""
Runtime
1188 ms

Memory
25 MB
"""

prices = [7,1,5,3,6,4]

max_profit = 0
min_price = prices[0]

for i in range(1, len(prices)):
    price = prices[i]
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)

print(max_profit)




"""
Runtime
1058 ms

Memory
24.9 MB
"""


def func(prices):
    buy = prices[0]
    profit = 0
    for i in prices[1:]:
        if i - buy > 0:
            profit = max(profit, i - buy)
        else:
            buy = i
    return profit

print(func(prices))