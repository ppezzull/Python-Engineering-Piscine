import sys

def ft_max(list):
  max = list[0]
  for n in list:
    if n > max:
        max = n
  return max

argc = len(sys.argv)
if argc == 4:
  n1 = float(sys.argv[1])
  n2 = float(sys.argv[2])
  n3 = float(sys.argv[3])
  print(f"The max is: {ft_max([n1,n2,n3])}")
else:
  print("Error! Usage: python3 ft_max.py <x> <y> <z>")