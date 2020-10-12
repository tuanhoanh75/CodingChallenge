def getUserInput():
    while True:
        try:
            firstStock = \
                list(map(int,
                         input("Enter the prices for your 1st stock separated by space: ").strip().split()))
            if 1 <= len(firstStock) <= 100000:
                print("Your first list of stock prices: ", firstStock)
            else:
                print("Warning!: The list size doesn't meet the requirements! "
                      "Please note: Your inputs = = number of days and the given limit is 1 to 100000 days!\n")
                continue
        except Exception as e:
            print(e, "\n")
        else:
            while True:
                try:
                    secondStock = \
                        list(map(int,
                                 input("\nEnter the prices for your 2nd stock separated by space: ").strip().split()))
                    if 1 <= len(secondStock) <= 100000:
                        print("Your second list of stock prices: ", secondStock)
                    else:
                        print("Warning!: The list size doesn't meet the requirements! "
                              "Please note: Your inputs == number of days and the given limit is 1 to 100000 days!\n")
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

    listobj = check_rules()
