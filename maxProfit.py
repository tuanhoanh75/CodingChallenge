def buy_and_sell(price, start, end):
    if end <= start:
        return 0

    # Initialise the profit
    profit = 0

    # The day at which the stock must be bought
    for i in range(start, end, 1):

        # The day at which the stock must be sold
        for j in range(i+1, end+1):

            # If buying the stock at ith day and selling it at jth day is profitable
            if (price[j] > price[i]):

                curr_profit_1 = price[j] - price[i]
                print("Print current profit 1: ", curr_profit_1)
                curr_profit_2 = buy_and_sell(price, start, i - 1)
                curr_profit_3 = buy_and_sell(price, j + 1, end)

                # Update the current profit
                # curr_profit = curr_profit_1 + curr_profit_2 + curr_profit_3

                # Update the maximum profit so far
                profit = max(profit, curr_profit_1)
                #print("Print profit:", profit)

    return profit


if __name__ == '__main__':
    price = list(map(int, input("\nEnter your list of stock prices: ").strip().split()))
    n = len(price)

    print("\nYour max. profit: ", buy_and_sell(price, 0, n-1))
