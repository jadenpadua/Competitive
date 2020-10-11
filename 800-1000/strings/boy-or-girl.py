def main():
    s = input()
    uniques = len(set(s))

    if uniques % 2 == 1:
        return "IGNORE HIM!"
    else:
        return "CHAT WITH HER!"

print(main())