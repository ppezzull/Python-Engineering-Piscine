import sys

if __name__ == "__main__":
  n = int(input("Insert an integer: "))
  file = open(sys.path[0] + "/words.txt", 'r')
  print(f"The words longer than {n} are the following:")
  for word in [word[:-1] for word in file if len(word[:-1]) > n]:
    print(word)