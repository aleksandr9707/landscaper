def main():
    money = 0
    has_scissors = False

    print("Welcome to your landscaping business!")

    while True:
        print("Current balance: $", money)
        print("Options:")
        print("1. Cut lawns")
        print("2. Buy rusty scissors ($5)")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            if has_scissors:
                money += 5
                print("You spent the day cutting lawns and earned $5.")
            else:
                money += 1
                print("You spent the day cutting lawns and earned $1.")
        elif choice == "2":
            if has_scissors:
                print("You already have scissors.")
            elif money >= 5:
                money -= 5
                has_scissors = True
                print("Congratulations! You bought a pair of rusty scissors.")
            else:
                print("Sorry, you don't have enough money to buy scissors.")
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == '__main__':
    main()

