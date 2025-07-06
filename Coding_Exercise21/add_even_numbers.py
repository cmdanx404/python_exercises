def sum_even_numbers():
    total = 0
    for number in range(1, 101):  # from 1 to 100 inclusive
        if number % 2 == 0:       # check if the number is even
            total += number
    return total

# Example usage:
result = sum_even_numbers()
print("Sum of even numbers from 1 to 100:", result)
