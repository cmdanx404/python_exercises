import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Are the numbers close?", math.isclose(a, b, rel_tol=1e-4))
