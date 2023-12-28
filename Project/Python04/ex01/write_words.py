import sys

if __name__ == "__main__":
  n = int(input("Insert an integer: "))
  file = open(sys.path[0] + "/words.txt", 'r')
  new_file = open(sys.path[0] + "/long_words.txt", "w")
  for word in [word for word in file if len(word) > n]:
    new_file.write(word)
  print(f'The words longer than {n} have been written on "long_words.txt"')
