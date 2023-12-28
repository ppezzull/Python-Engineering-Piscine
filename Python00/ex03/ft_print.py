string = input("Insert string: ")
n = int(input("Insert an integer: "))
if len(string) > (-n if n < 0 else n):
    print(f"{string[n]} {string[-n]}")
else:
    print("Error: index out of range")

