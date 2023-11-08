from colorama import Fore

print("Percentage Evaluator".center(31, '-'))
print("|  PERCENTAGE  |   CATEGORY   |")
print("|" + "< 40 ".center(14) + "|" + Fore.RED + "Poor".center(14) + Fore.WHITE +  "|")
print("|" + ">= 40 & <55 ".center(14) + "|" + Fore.MAGENTA +  "Fair".center(14) + Fore.WHITE +  "|")
print("|" + ">= 55 & <65 ".center(14) + "|" + Fore.YELLOW +  "Satisfactory".center(14) + Fore.WHITE +  "|")
print("|" + ">= 65 ".center(14) + "|" + Fore.GREEN + "Best".center(14) + Fore.WHITE + "|")

while True:
    try:
        percent_input = int(input("\nEnter percentage(%): "))
        if percent_input < 40:
            print("Evaluation:" + Fore.RED +  "POOR" + Fore.WHITE)
        if percent_input in range(40, 55):
            print("Evaluation:" + Fore.MAGENTA +  "FAIR" + Fore.WHITE)
        if percent_input in range(55, 65):
            print("Evaluation:" + Fore.YELLOW +  "SATISFACTORY" + Fore.WHITE)
        if percent_input >= 65:
            print("Evaluation:" + Fore.GREEN +  "BEST" + Fore.WHITE)
        break
    except:
        print("\nInput should be a whole number!")
