def find_max_and_min():
    max_num = None
    min_num = None

    while True:
        user_input = input("Enter a number (or 'done'): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            if max_num is None or number > max_num:
                max_num = number
            if min_num is None or number < min_num:
                min_num = number
        except ValueError:
            print("Invalid input.")

    if max_num is not None:
        print("Maximum:", max_num)
        print("Minimum:", min_num)
    else:
        print("No valid numbers were entered.")
