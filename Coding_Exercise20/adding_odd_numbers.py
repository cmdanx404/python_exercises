def sum_odd_numbers():
    total = 0
    for number in range(1, 101):  # from 1 to 100 inclusive
        if number % 2 != 0:       # check if the number is odd
            total += number
    return total

# Example usage:
result = sum_odd_numbers()
print("Sum of odd numbers from 1 to 100:", result)
