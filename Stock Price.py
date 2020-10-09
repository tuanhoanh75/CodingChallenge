def InputStockPrices():
    while True:
        try:
            firstStock = \
                list(map(int,
                         input("Enter the prices for your 1st stock separated by space: ").strip().split()))
        except:
            print("Message is raised due to invalid values. Please try again!\n")
        else:
            while True:
                try:
                    secondStock = \
                        list(map(int,
                                 input("Enter the prices for your 2nd stock separated by space: ").strip().split()))
                except:
                    print("Message is raised due to invalid values. Please try again!\n")

                else:
                    print("\nYour First stock prices: ", firstStock)
                    print("Your second stock prices: ", secondStock)
                    return [firstStock, secondStock]

# def check_limitation(firstStock, secondStock):


def calculateProfit(firstStock, secondStock):
    return 1


if __name__ == '__main__':
    print("-------------------------------------------------------------------------------------")
    print("Calculating the maximum profit by given prices of two stocks during multiple days.")
    print("Rules: (A) You can buy / sell stocks anytime, but can only hold 1 share of any stocks!")
    print("       (B) Numbers of days is limited from 1 to 100000 days.")
    print("       (C) Each price is an integer number from 1 to 1000.")
    print("-------------------------------------------------------------------------------------\n")

    test = InputStockPrices()

    firstStock = None
    secondStock = None

    for i in test:
        firstStock = i
        secondStock = i

    print("1st Stock: ", firstStock)
    print("2nd Stock: ", secondStock)
