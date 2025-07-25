import math

mode = input("Convert from (1) dBm to mW or (2) mW to dBm? Enter 1 or 2: ")

if mode == "1":
    dBm = float(input("Enter dBm: "))
    mW = math.pow(10, dBm / 10)
    print("Power in milliwatts:", round(mW, 4))
else:
    mW = float(input("Enter mW: "))
    dBm = 10 * math.log10(mW)
    print("Power in dBm:", round(dBm, 2))
