import math

P = float(input("Principal amount: "))
r = float(input("Annual interest rate (in %): ")) / 100
t = int(input("Time in years: "))

A = P * math.pow((1 + r), t)
print("Estimated total after", t, "years is:", round(A, 2))
