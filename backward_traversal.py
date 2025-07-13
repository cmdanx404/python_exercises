# Coding Exercise No.28
# Backward Traversal

def print_letters_backwards():
    user_input = input("Enter a string: ")
    length = len(user_input)
    for i in range(length - 1, -1, -1):
        print(user_input[i])

print_letters_backwards()
