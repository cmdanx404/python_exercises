import math

print("\nWelcome to Factorial Calculator!\n")

while True:
    num = input("Enter a non-negative integer: ")

    if not num.isdigit():
        print("Invalid input. Please enter a non-negative integer.\n")
        continue

    num = int(num)
    result = math.factorial(num)
    print(f"Factorial of {num} is {result}\n")

    again = input("Do you want to calculate another factorial? (Y/N): ").strip().lower()
    if again != 'y':
        print("Goodbye!")
        break
