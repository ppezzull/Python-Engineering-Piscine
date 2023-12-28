string = input("Insert string: ")
length = len(string)
if length < 20:
  print(f'{" " * (20 - length)}{string}')
else:
  print(string[length - 20:])