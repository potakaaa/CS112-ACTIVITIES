# Helbiro
start, stop, test = 1, 11, True
while test:
    print(f"\033[1;37mMULTIPLICATION TABLE FROM {start} - {stop - 1}".center(90))
    print()
    print("\033[1;31m0\033[0;37m   |\t", end="")
    for i in range(start, stop):
        print(f"\033[1;33m{i}\033[0;37m" , end="\t")
    print()
    print("-"*4 + "+" + "-"*78)
    for j in range(1, 11):
        if j == 10:
            print(f"\033[1;32m{j}\033[0;37m  |", end="\t")
        else:
            print(f"\033[1;32m{j}\033[0;37m   |", end="\t")
        for x in range(start, stop):
            print(j * x, end="\t")
        print()
    print()
    while True:
        try:
            ask = int(input("Continue? [0: No / 1: Yes]: "))
            if ask == 0:
                test = False
                break
            elif ask == 1:
                start += 10
                stop += 10
                print()
                break
            else:
                print("\033[1;31mInput should be 0 or 1\033[0;37m")
                print()
        except:
            print("\033[1;31mInvalid input!\033[0;37m")
            print()

    