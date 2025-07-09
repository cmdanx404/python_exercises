# Coding Exercises No.23
# Numbers divisible by five

def numbers_divisible_byfive(p_list):
    for num in (p_list):
        if num > 130:
            print("STOP")
            break
        if num % 5 == 0:
            print(num)

mylist = [10, 30, 55, 64, 80, 92, 105, 125, 131, 180]
numbers_divisible_byfive(mylist)



