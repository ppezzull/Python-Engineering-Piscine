def sum_list(list):
  sum = 0
  for n in list:
    sum += n
  return sum

def get_list(list=[]):
  n = int(input("Insert integer: "))
  if n == 0:
    return list
  else:
    list.append(n)
    return get_list(list)

if __name__ == "__main__":
  print(sum_list(get_list()))
  