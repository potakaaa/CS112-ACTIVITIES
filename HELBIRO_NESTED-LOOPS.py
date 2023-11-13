# Helbiro
import time, random

print("\033[1;33mName Reducer\033[0;37m".center(60))
while True:
    name = input("\033[1;37mEnter your name: \033[0;37m").upper()
    x = len(name)
    print()
    if not name.strip():
        print("\033[1;31mInvalid input! Blanks are not allowed\033[0;37m")
        print()
    elif any(char.isdigit() for char in name):
        print("\033[1;31mInvalid input! Numeric characters are not allowed\033[0;37m")
        print()
    else:
        for i in range(0, len(name)):
            for j in range(0, x):
                color = random.randint(31, 37)
                print(f"\033[0;{color}m{name[j]}\033[0;37m\t", end="")
                time.sleep(0.15)
            print()
            x -= 1

        print(f"\033[0;37mHello, \033[1;33m{name}\033[0;37m!")
        break
