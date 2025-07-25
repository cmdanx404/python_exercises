import math

password = input("Enter your password: ")
entropy = len(password) * math.log2(94)  # assuming 94 printable ASCII characters
print("Estimated password entropy:", round(entropy, 2), "bits")
