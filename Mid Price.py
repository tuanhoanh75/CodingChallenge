def checkInput(mid, bid):
    if 1 <= bid < mid <= 1000:
        return mid, bid
    else:
        print("\nWarning: One of your entered input value is violating the given limitation.")
        print("Please check and correct you input price!\n")

        new_mid = int(input("Re-enter your mid price: "))
        new_bid = int(input("Re-enter your bid price: "))
        res = checkInput(new_mid, new_bid)

        return res


def calculatePrice(midPrice, bidPrice):
    askPrice = (midPrice * 2) - bidPrice
    return askPrice


if __name__ == '__main__':

    print("------------------------------------------------------------")
    print("Please enter your mid/bid price to calculate the ask price.")
    print("Note: 1 <= bidPrice < midPrice <= 1000")
    print("------------------------------------------------------------\n")

    mid = int(input("FIRST, enter your mid price: "))
    bid = int(input("\nSECOND, enter your bid price: "))
    check = checkInput(mid, bid)

    ask = calculatePrice(mid, bid)
    print("\nThe calculated ask price is: ", ask)
