def getUserInput():
    while True:
        try:
            firstStock = \
                list(map(int,
                         input("Enter your 1st list of stock prices separated by space: ").strip().split()))

            size_limit = all(i in range(1, 1001) for i in firstStock)
            n_days = len(firstStock) in range(1, 100001)

            if n_days and size_limit:
                print("Your first list of stock prices: ", firstStock)
            else:
                print("\nAttention: Your list contains values that doesn't meet the given requirements! "
                      "Please try again.")
                continue
        except Exception as e:
            print(e, "\n")
        else:
            while True:
                try:
                    secondStock = \
                        list(map(int,
                                 input("\nEnter your 2nd list of stock prices separated by space: ").strip().split()))

                    size_limit = all(i in range(1, 1001) for i in secondStock)
                    n_days = len(secondStock) in range(1, 100001)

                    if n_days and size_limit:
                        print("Your second list of stock prices: ", secondStock)
                    else:
                        print("Attention: Your list contains values that doesn't meet the given requirements! "
                              "Please try again.")
                        continue
                except Exception as e:
                    print(e)
                else:
                    return [firstStock, secondStock]


def calculateProfit(firstStock, secondStock):
    return 1


if __name__ == '__main__':
    print("-------------------------------------------------------------------------------------")
    print("Calculating the maximum profit by given prices of two stocks during multiple days.")
    print("Rules: (A) You can buy / sell stocks anytime, but can only hold 1 share of any stocks!")
    print("       (B) Numbers of days is limited from 1 to 100000 days.")
    print("       (C) Each price is an integer number from 1 to 1000.")
    print("-------------------------------------------------------------------------------------\n")

    listobj = getUserInput()
    first, second = listobj

    print("\nFirst Stock: ", first)
    print("Second Stock: ", second)