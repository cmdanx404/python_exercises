numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []

chunk_size = 3

for i in range(0, len(numbers), chunk_size):
    chunk = numbers[i:i + chunk_size]
    result.extend(chunk[::-1])

print("Original list:", numbers)
print("Processed list:", result)
