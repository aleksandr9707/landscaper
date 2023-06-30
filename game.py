def main():
    money = 0
    has_scissors = False
    has_lawnmower = False
    has_fancy_lawnmower = False
    has_students = False

    print("Welcome to your landscaping business!")

    while True:
        print("Current balance: $", money)
        print("Options:")
        print("1. Cut lawns")
        print("2. Buy rusty scissors ($5)")
        print("3. Buy old-timey push lawnmower ($25)")
        print("4. Buy a fancy battery-powered lawnmower ($250)")
        print("5. Buy a  team of starving students ($500)")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            if has_students:
                money +=250
                print("You spent the day relaxing while a team of starving students mowed your lawn. You made $250")
            elif has_fancy_lawnmower:
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

            if money >= 1000 and has_students:
                print("Congratulations! You have a team of starving students and $1000. You've won the game!")
                break
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
            if has_students:
                print("You already have a team of starving students.")
            elif money >= 500:
                money -= 500
                has_students = True
                print("Congratulations! You hired a team of starving students.")
            else:
                print("Sorry, you don't have enough money to hire a team of starving students") 
        elif choice == "6":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")
        

if __name__ == '__main__':
    main()



