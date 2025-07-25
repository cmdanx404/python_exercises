import math

n = int(input("Enter total number of items (n): "))
k = int(input("Enter number of items to choose (k): "))

if k <= n:
    print(f"Combinations: {math.comb(n, k)}")
else:
    print("k must be less than or equal to n.")
