import sys

argc = len(sys.argv)
if argc == 3:
  n1 = float(sys.argv[1])
  n2 = float(sys.argv[2])
  if n1 > n2:
    print(f"{n1} is greater than {n2}")
  elif n1 < n2:
    print(f"{n1} is less than {n2}")
  else:
    print(f"{n1} is equal than {n2}")
