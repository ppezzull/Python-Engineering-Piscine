import sys

def sort_lst(lst):
  i = 0
  while i < len(lst):
    j = 0
    while j < len(lst):
      if lst[i] < lst[j]:
        lst[i], lst[j] = lst[j], lst[i]
      j += 1
    i += 1
  return lst

if __name__ == "__main__":
  argc = len(sys.argv)
  if argc == 2:
    print("Char count:")
    ordered_letters = sort_lst([letter.lower() for letter in sys.argv[1]])
    i = 0
    while i < len(ordered_letters) - 1:
      count = 1
      while (
        i + count < len(ordered_letters) and 
        ordered_letters[i] == ordered_letters[i + count]
      ):
        count += 1
      print(f"{ordered_letters[i]} = {count}")
      i += count
  elif argc == 1:
    print("Error! No string given")
  else:
    print("Error! Too many strings given")
