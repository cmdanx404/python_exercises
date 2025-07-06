def sum_above_average(scores):
    # Calculate total sum and count manually
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1

    if count == 0:
        return 0  # Avoid division by zero

    # Calculate average
    average = total / count

    # Sum scores above average
    sum_above = 0
    for score in scores:
        if score > average:
            sum_above += score

    return sum_above

# Example usage:
scores = [70, 85, 90, 60, 75]
result = sum_above_average(scores)
print("Sum of scores above average:", result)
