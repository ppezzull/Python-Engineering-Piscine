import sys

argc = len(sys.argv)
if argc == 2:
  if sys.argv[1] == sys.argv[1][::-1]:
    print(f"The string {sys.argv[1]} is a palindrome")
  else: 
    print(f"The string {sys.argv[1]} is not a palindrome")
else:
  print(f"Error! Insert just 1 string!")