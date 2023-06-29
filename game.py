def main():
    money = 0

    print("Welcome to your landscaping business!")

    while True:
        print("Current balance: $", money)
        print("Options:")
        print("1. Cut lawns")
        print("2. Quit")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            money += 1
            print("You spent the day cutting lawns and earned $1.")
        elif choice == "2":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == '__main__':
    main()

