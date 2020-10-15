def buy_and_sell(stock_price):
    n = len(stock_price)

    # Create profit array and initialize it as 0
    profit = [0]*n

    # Get the maximum profit with only one tx allowed
    # After this loop. profit[i] contains maximum
    # profit from price[i...n-1] using at most one tx.
    max_price = stock_price[n - 1]

    for i in range(n-2, 0, -1):

        if stock_price[i] > max_price:
            max_price = stock_price[i]

        # we can get profit[i] by taking maximum of:
        # a) previous maximum, i.e., profit[i+1]
        # b) profit by buying at price[i] and selling at max_price
        profit[i] = max(profit[i+1], max_price - stock_price[i])

    # Get the maximum profit with two tx allowed
    # After this loop, profit[n-1] contains the result
    min_price = stock_price[0]

    for i in range(1, n):
        if stock_price[i] < min_price:
            min_price = stock_price[i]

        # Maximum profit is maximum of:
        # a) previous maximum, i.e., profit[i-1]
        # b) (Buy, Sell) at (min_price, A[i]) and add
        #    profit of other tx stored in profit[i]
        profit[i] = max(profit[i-1], profit[i] + (stock_price[i] - min_price))

    result = profit[n-1]
    return result


if __name__ == '__main__':
    stock_price = list(map(int, input("\nEnter your list of stock prices: ").strip().split()))

    print("Max. profit: ", buy_and_sell(stock_price))

