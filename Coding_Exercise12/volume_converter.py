# Coding Exercise No.12
# Volume converter

vol_in_ounce = float(input("Enter volume in Ounce: "))

vol_in_mil = 29.57353 # for every 1 ounce
 
Output = round((vol_in_ounce * vol_in_mil),5)

print(f"Volume in mililiters (ml): {Output} ")


