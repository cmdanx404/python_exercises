# Coding Exercise No.9
# Coin Toss

import random

print("Welcome to the Virtual Coin Toss!")

start = input("Do you want to start tossing the coin? (Y/N): ").strip().lower()
if start != 'y':
    print("Exiting the program. Goodbye!")
else:
    heads_count = 0
    tails_count = 0

    while True:
        toss = random.randint(0, 1)

        if toss == 1:
            print("\nResult: Heads")
            heads_count += 1
        else:
            print("\nResult: Tails")
            tails_count += 1

        again = input("\nDo you want to toss again? (Y/N): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing!")
            print(f"Total Heads: {heads_count}")
            print(f"Total Tails: {tails_count}")
            print("Goodbye!")
            break
