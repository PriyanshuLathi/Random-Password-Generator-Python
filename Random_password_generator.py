import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},:;.-/\\?+*#@<>!$%^&_"

upper, lower, nums, syms = True, True, True, True

def get_user_input(prompt):
    while True:
        char1 = input(prompt).strip().upper()
        if char1 == 'Y':
            return True
        elif char1 == 'N':
            return False
        else:
            print("Invalid Input. Please try again.")

upper = get_user_input("Do you want to include uppercase letters? [Y/N]: ")
lower = get_user_input("Do you want to include lowercase letters? [Y/N]: ")
nums = get_user_input("Do you want to include numbers? [Y/N]: ")
syms = get_user_input("Do you want to include symbols? [Y/N]: ")

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

if not all:
    print("No characters selected. Cannot generate passwords.")
else:
    length = int(input("Enter the length of password: "))
    amount = int(input("Enter the number of passwords you want to generate: "))

    if length > len(all):
        print("Length exceeds the number of available characters. Automatically adjusting length to fit.")
        length = len(all)

    for _ in range(amount):
        password = "".join(random.choices(all, k=length))
        print(password)