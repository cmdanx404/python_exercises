# Coding Exercise No.13
# Painting the Wall

import math

def calculate_paint(h, w):
    Area = (h * w)
    cans = math.ceil(Area / 4)
    print(f"Number of cans needed to paint the wall: {cans} cans")

height = int(input("Enter the wall height: "))
width = int(input("Enter the wall height: "))

calculate_paint(h = height, w = width)


