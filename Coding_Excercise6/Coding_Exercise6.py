# Coding Exercise No.6
# BMI Calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = round(weight / (height * height), 1)

if BMI < 18.5:
    print(f"BMI = {BMI} kg/m² (Underweight)")
elif BMI < 25.0:
    print(f"BMI = {BMI} kg/m² (Normal)")
elif BMI < 30.0:
    print(f"BMI = {BMI} kg/m² (Overweight)")
elif BMI < 35.0:
    print(f"BMI = {BMI} kg/m² (Obese)")
else:
    print(f"BMI = {BMI} kg/m² (Severely Obese)")

    
    


    
