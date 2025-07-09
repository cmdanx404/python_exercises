# Coding Exercise No.24
# Factorial Using Function

def factorial(p_num):
    result = 1
    if p_num == 0:
        return("The Factorial of 0 is 1.")
    elif p_num < 0:
        return("Factorial does not exist for negative numbers.")
    else:
        for i in range(2, p_num + 1):
            result *= i
        return(f"The Factorial of {p_num} is {result}.")

user_input = int(input("Enter a non-negative integer: "))
print(factorial(user_input))

