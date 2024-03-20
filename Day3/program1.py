def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    max_profit = 0
    profit = [0] * n

      min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit[i] = max(profit[i - 1], prices[i] - min_price)

    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, profit[i] + max_price - prices[i])

    return max_profit


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print("Maximum profit:", max_profit(prices))
