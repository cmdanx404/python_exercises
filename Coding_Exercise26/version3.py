def find_max_and_min():
    nums = []

    while True:
        val = input("Enter a number (or 'done'): ").strip().lower()
        if val == 'done':
            break
        try:
            nums.append(float(val))
        except ValueError:
            print("Invalid input.")

    if nums:
        print(f"Maximum: {max(nums)}\nMinimum: {min(nums)}")
    else:
        print("No valid numbers entered.")
