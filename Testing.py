def buy_and_sell(stock_price):
    n = len(stock_price)
    profit = [0]*n

    max_price = stock_price[n - 1]
    print(max_price)

    for i in range(n-2, 0, -1):
        if stock_price[i] > max_price:
            max_price = stock_price[i]

        profit[i] = max(profit[i+1], max_price - stock_price[i])
        print(profit)

    min_price = stock_price[0]
    print("\n", min_price)

    for i in range(0, n):
        if stock_price[i] < min_price:
            min_price = stock_price[i]

        profit[i] = max(profit[i-1], profit[i] + (stock_price[i] - min_price))
        print(profit)

    result = profit[n-1]
    return result


if __name__ == '__main__':
    stock_price = list(map(int, input("\nEnter your list of stock prices: ").strip().split()))

    print("Max. profit: ", buy_and_sell(stock_price))

