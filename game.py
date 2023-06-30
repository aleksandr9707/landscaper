def main():
    money = 0
    has_scissors = False
    has_lawnmower = False
    has_fancy_lawnmower = False

    print("Welcome to your landscaping business!")

    while True:
        print("Current balance: $", money)
        print("Options:")
        print("1. Cut lawns")
        print("2. Buy rusty scissors ($5)")
        print("3. Buy old-timey push lawnmower ($25)")
        print("4. Buy a fancy battery-powered lawnmower ($250)")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if has_fancy_lawnmower:
                money += 100
                print("You spent the day cutting lawns with your fancy lawnmower and earned $100.")
            elif has_lawnmower:
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
            if has_fancy_lawnmower:
                print("You already have a fancy lawnmower.")
            elif money >= 250:
                money -= 250
                has_fancy_lawnmower = True
                print("Congratulations! You bought an fancy battery-powered lawnmower.")
            else:
                print("Sorry, you don't have enough money to buy a fancy battery-powered lawnmower.") 

        elif choice == "5":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == '__main__':
    main()



