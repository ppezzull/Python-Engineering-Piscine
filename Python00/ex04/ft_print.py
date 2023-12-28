string = input("Insert string: ")
n = int(input("Insert an integer: "))
if len(string) > n and n >= 0:
    print(f"{string[n:-n]}")
else:
    print()