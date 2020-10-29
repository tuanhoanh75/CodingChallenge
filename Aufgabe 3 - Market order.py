def check_input():
    while True:
        try:
            volume = list(map(int, input("Enter your order volumes: ").strip().split()))
            vol_size = len(volume) in range(100)
            numb_limit = all(i in range(2, 51) for i in volume)

            if numb_limit and vol_size:
                print("\nYour given volumes =", volume, "\n")
            else:
                print("Attention: The order list doesn't meet the given requirements! Please try again.\n")
                continue
        except Exception as e:
            print(e, "\n")
        else:
            return volume


def countTraders(volumes):
    if not volumes:
        return 0

    n_trader = 0
    vol = []

    for i in range(2, max(volumes)+1):
        x = i
        print("Current X =", x)

        set = []
        for j in volumes:
            if (j % x) == 0:
                set.append(j)

        print("Subset =", set)




if __name__ == '__main__':
    print("----------------------------------------------------------------------------")
    print("Please enter the order volumes.")
    print("Limitation: A) There are at most 100 order volumes on market")
    print("            B) Each volume is an integer number between 2 and 50 inclusive")
    print("----------------------------------------------------------------------------\n")

    volumes = check_input()

    print("\ntraders =", countTraders(volumes))
