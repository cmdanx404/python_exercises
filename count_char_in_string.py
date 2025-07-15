def count_character_in_string(text, character):
    return text.count(character)

user_input = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")

if len(char_to_count) != 1:
    print("Please enter exactly one character.")
else:
    result = count_character_in_string(user_input, char_to_count)
    print(f"The character '{char_to_count}' appears {result} time(s) in the string.")
