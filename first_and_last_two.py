def print_first_and_last_two(text):
    if len(text) < 2:
        print("The input is too short (less than 2 characters).")
    else:
        result = text[:2] + text[-2:]
        print("First 2 and last 2 characters:", result)

user_input = input("Enter a string: ")
print_first_and_last_two(user_input)
