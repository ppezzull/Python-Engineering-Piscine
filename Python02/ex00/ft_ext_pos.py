import sys

argc = len(sys.argv)
if argc > 2:
  i = 1
  max = 0
  min = 1e100
  pos_max = 0 
  pos_min = 0
  while i < len(sys.argv):
    n = int(sys.argv[i])
    if n > max:
      max = n
      pos_max = i-1
    if n < min:
      min = n
      pos_min = i-1
    i += 1
  print(f"The min is {min} and its position is {pos_min}")
  print(f"The max is {max} and its position is {pos_max}")
else:
  print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
