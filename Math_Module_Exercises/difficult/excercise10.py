import math

n = int(input("Enter a number: "))
if n > 1:
    estimated_primes = n / math.log(n)
    print(f"Estimated number of primes ≤ {n}:", int(estimated_primes))
else:
    print("Enter a number greater than 1.")
