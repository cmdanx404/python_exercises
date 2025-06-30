# Coding Exercise No.11
# Area of Square

print("Welcome to Area of Square calculator\n")

def Area_Square(side):
    area = round((side * side), 2)
    print(f"Area of the Square is: {area}")

while True:
    try:
        side = float(input("Enter Side of the Square: "))
        Area_Square(side)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    again = input("Would you like to calculate again? (Y/N): ").strip().upper()
    if again != "Y":
        print("Thank you for using Area of Square Calculator. Goodbye!")
        break
