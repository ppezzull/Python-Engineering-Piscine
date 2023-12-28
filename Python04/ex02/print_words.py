import sys

if __name__ == "__main__":
  n = int(input("Insert an integer: "))
  file_name = input("Insert an integer: ")
  try:
    file = open(sys.path[0] + "/" + file_name, 'r')
    print(f"The words longer than {n} are the following:")
    for word in [word[:-1] for word in file if len(word[:-1]) > n]:
      print(word)
  except:
    print("Error! The specified file does not exist!")