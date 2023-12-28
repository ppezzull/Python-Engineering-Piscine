import sys

def trim(array):
  pass

if __name__ == "__main__":
  argc = len(sys.argv)
  if argc > 2:
    print(f"The new list is: {sys.argv[2:-1]}")
  else:
    print("Error! You must insert at least 2 values")