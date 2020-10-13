while True:
    try:
        print("\nTo enter a youth club in groups, it is mandatory to verify the age of each person.\n"
              "The age restriction: From 17 to 21.\n"
              "If at least one person from the group is a minor, then admission will be denied!\n"
              "----------------------------------------------------------------------------------")

        age = list(map(int, input("\nThe list of age separated by space: ").strip().split()))
        check = all(17 <= i <= 21 for i in age)
        print("Return: ", check)
    except Exception as e:
        print(e)
    else:
        exit(0)
