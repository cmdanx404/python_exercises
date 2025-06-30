# Coding Excercie No. 18
# Find the Integers in a list ( Modified Version )

# Ask the user to enter values separated by spaces and/or commas
user_input = input("Enter values separated by spaces and/or commas:\n> ")

# Ask the user to choose an option
print("\nSelect how to extract integers:")
print("1. Only positive integers")
print("2. Include negative integers")
print("3. Include floats (rounded) and treat them as integers")
print("4. Include numeric strings like '51' and treat them as integers")
choice = input("Enter 1, 2, 3, or 4:\n> ")

# Replace commas with spaces, then split the input string
raw_items = user_input.replace(',', ' ').split()

# Utility functions
def is_int_string(s):
    return s.lstrip('-').isdigit()

def is_float_string(s):
    if s.count('.') == 1:
        whole, decimal = s.split('.')
        return whole.lstrip('-').isdigit() and decimal.isdigit()
    return False

# Convert all valid entries into Python types: int, float, or leave as string
converted_list = [
    int(item) if is_int_string(item)
    else float(item) if is_float_string(item)
    else item
    for item in raw_items
]

# Create the final list based on the user's choice
if choice == '1':
    # Only positive integers
    final_list = [x for x in converted_list if type(x) == int and x > 0]

elif choice == '2':
    # Include negative integers too
    final_list = [x for x in converted_list if type(x) == int]

elif choice == '3':
    # Include ints and floats (rounded to nearest int)
    final_list = [
        x if type(x) == int else round(x)
        for x in converted_list
        if type(x) == int or type(x) == float
    ]

elif choice == '4':
    # Include ints and numeric strings like "51"
    final_list = []
    for item in raw_items:
        if is_int_string(item):
            final_list.append(int(item))  # includes numeric strings too
        elif is_float_string(item):
            continue  # skip floats
        else:
            try:
                # If not already processed, check if it's a numeric string like "51"
                final_list.append(int(item.strip('"').strip("'")))
            except:
                continue

else:
    print("\nInvalid option selected.")
    final_list = []

# Output result
print("\nFinal list of integers:")
print(final_list)
