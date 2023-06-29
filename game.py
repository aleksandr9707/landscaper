def main():
    money = 0
    has_scissors = False
    has_lawnmower = False

    print("Welcome to your landscaping business!")

    while True:
        print("Current balance: $", money)
        print("Options:")
        print("1. Cut lawns")
        print("2. Buy rusty scissors ($5)")
        print("3. Buy old-timey push lawnmower ($25)")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if has_lawnmower:
                money += 50
                print("You spent the day cutting lawns with your lawnmower and earned $50.")
            elif has_scissors:
                money += 5
                print("You spent the day cutting lawns with your scissors and earned $5.")
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
            if has_lawnmower:
                print("You already have a lawnmower.")
            elif money >= 25:
                money -= 25
                has_lawnmower = True
                print("Congratulations! You bought an old-timey push lawnmower.")
            else:
                print("Sorry, you don't have enough money to buy a lawnmower.")
        elif choice == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == '__main__':
    main()



