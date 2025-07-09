# Coding Exercise No.25
# Sum, Count, Average of Entered Number

total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break

    try:
        number =  float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input, enter numeric value only.")

if count > 0:
    average = total / count
    print("Count:", count)
    print("Total:", total)
    print("Average:", average)

else:
    print("No valid input, closing the program...")