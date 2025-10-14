from collections import deque

def bfs_max_profit(prices):
    n = len(prices)
    max_profit = 0
    queue = deque()
    
    # (day, holding, profit)
    # holding = -1 means no stock held; otherwise, it's the index we bought at
    queue.append((0, -1, 0))

    while queue:
        day, holding, profit = queue.popleft()

        if day == n:
            max_profit = max(max_profit, profit)
            continue

        # Option 1: Do nothing
        queue.append((day + 1, holding, profit))

        # Option 2: Buy (if not holding)
        if holding == -1:
            queue.append((day + 1, day, profit))

        # Option 3: Sell (if holding)
        elif holding != -1:
            gain = prices[day] - prices[holding]
            queue.append((day + 1, -1, profit + gain))

    return max_profit

# Sample stock prices over 5 days
stock_prices = [100, 180, 260, 310, 40, 535, 695]

print("Max profit using BFS:", bfs_max_profit(stock_prices))
