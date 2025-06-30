# Coding Excersie No.16
# Calculator

n1 = int(input("What is the first number? "))
n2 = int(input("What is the second number? "))

operation = input("Pick operation from this list (+,-,*,/) ")

if operation == "+":
    result = n1 + n2
elif operation == "-":
    result = n1 - n2
elif operation == "*":
    result = n1 * n2
elif operation == "/":
    result = n1 / n2
else:
    print("Error: invalid operation")

print(f"{n1} {operation} {n2} = {result}")
