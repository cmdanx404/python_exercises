# Coding Exercise No.7
# Burger Order with validation and loop

while True:
    print("\nWelcome to Burger Shop!")

    # Get burger size
    size = input("""\nWhat size of burger do you want?
Please Type:
M for Mini
N for Normal
L for Large\n""").upper()

    if size not in ["M", "N", "L"]:
        print("❌ Invalid input for burger size. Please try again.")
        continue  # restart loop

    # Get mushroom choice
    mushroom = input("Do you want mushroom? Y/N?\n").upper()
    if mushroom not in ["Y", "N"]:
        print("❌ Invalid input for mushroom option. Please try again.")
        continue  # restart loop

    # Get cheese choice
    cheese = input("Do you want cheese? Y/N?\n").upper()
    if cheese not in ["Y", "N"]:
        print("❌ Invalid input for cheese option. Please try again.")
        continue  # restart loop

    # Calculate bill
    bill = 0

    if size == "M":
        bill += 5
        if mushroom == "Y":
            bill += 1
    elif size == "N":
        bill += 8
        if mushroom == "Y":
            bill += 1
    elif size == "L":
        bill += 10
        if mushroom == "Y":
            bill += 2

    if cheese == "Y":
        bill += 1

    # Print final bill
    print(f"\n✅ Your final bill is: ${bill}.")

    # Ask to order again or exit
    again = input("\nWould you like to place another order? (Y to continue, any other key to exit): ").upper()
    if again != "Y":
        print("Thank you for visiting Burger Shop! 🍔")
        break
