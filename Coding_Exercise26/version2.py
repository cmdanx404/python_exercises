def find_max_and_min():
    max_num = float('-inf')
    min_num = float('inf')
    found = False

    while True:
        val = input("Enter a number (or 'done'): ").strip().lower()
        if val == 'done':
            break
        try:
            num = float(val)
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            found = True
        except ValueError:
            print("Invalid input.")

    if found:
        print(f"Maximum: {max_num}\nMinimum: {min_num}")
    else:
        print("No valid numbers entered.")
