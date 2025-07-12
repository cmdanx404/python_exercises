# Coding Exercise No.27
# Sum of two digit number

def get_two_digit_number():
    while True:
        user_input = input("Enter a 2-digit number: ").strip()
        if user_input.isdigit() and len(user_input) == 2:
            return user_input
        print("Invalid input: Please enter exactly 2 digits.")

def sum_of_digits(number_str):
    return int(number_str[0]) + int(number_str[1])

def main():
    while True:
        number_str = get_two_digit_number()
        result = sum_of_digits(number_str)
        print(f"The sum of the digits of {number_str} is {result}.")
        if input("Try again? (yes/no): ").strip().lower() != "yes":
            print("Program exited.")
            break

if __name__ == "__main__":
    main()

