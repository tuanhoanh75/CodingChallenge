def checkInputBid(bid, mid):
    i = 1
    while (i > bid) and (bid < mid):
        print("\nYour bid price must be greater or equal to one!")
        bid = int(input("Re-enter your bid price: "))
    return bid


def calculatePrice(midPrice, bidPrice):
    askPrice = (midPrice * 2) - bidPrice
    return askPrice


if __name__ == '__main__':

    print("------------------------------------------------------------")
    print("Please enter your mid/bid price to calculate the ask price.")
    print("Note: 1 <= bidPrice < midPrice <= 1000 ")
    print("------------------------------------------------------------\n")

    mid = int(input("First, enter your mid price: "))
    bid = int(input("Second, enter your bid price: "))
    checkInputBid(bid, mid)