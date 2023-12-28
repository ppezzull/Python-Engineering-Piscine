import pickle
import sys

if __name__ == "__main__":
  word_count = {}
  for line in open(sys.path[0] + "/words.txt", 'r') :
    for word in line.split():
      if len(word) in word_count.keys():
        word_count[len(word)] += 1
      else:
        word_count[len(word)] = 1
  word_count = dict(sorted(word_count.items()))
  pickle_file = open(sys.path[0] + "/word_count.pickle", "wb")
  pickle.dump(word_count, pickle_file)
