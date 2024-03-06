def maximized_stock_profit(prices):
    accum_profit = 0
    
    for i in range(1,len(prices)):
        # If the previous day's price is less than the price of the current day, we sell
        if(prices[i] > prices[i-1]):
            accum_profit += prices[i] - prices[i-1]
    return accum_profit

# Test case 1
prices1 = [7, 1, 5, 3, 6, 4]
output1 = maximized_stock_profit(prices1)
print("Test case 1:", output1)  # Output: 7

# Test case 2
prices2 = [1, 2, 3, 4, 5]
output2 = maximized_stock_profit(prices2)
print("Test case 2:", output2)  # Output: 4

# Test case 3
prices3 = [7, 6, 4, 3, 1]
output3 = maximized_stock_profit(prices3)
print("Test case 3:", output3)  # Output: 0