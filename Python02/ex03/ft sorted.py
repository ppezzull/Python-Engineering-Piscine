import sys
  
if __name__ == "__main__":
  argc = len(sys.argv)
  if argc > 2:
    array = [int(n) for n in sys.argv[1:]]
    if sorted(array, reverse=True) == array:
      print("The inserted sequence is sorted!")
    else:
      print("The inserted sequence is not sorted!")
      print(f"The correct order is {sorted(array, reverse=True)}")
  else:
    print("Error! You must insert at least 2 numbers")