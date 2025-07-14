# Coding Exercise No. 28
# Sum of Digits

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def main():
    user_input = input("Enter a positive integer: ")
    if user_input.isdigit():
        result = sum_of_digits(user_input)
        print(f"The sum of the digits is: {result}")
    else:
        print("Invalid input. Please enter a positive integer only.")

if __name__ == "__main__":
    main()
