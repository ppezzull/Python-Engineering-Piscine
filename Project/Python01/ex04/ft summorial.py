import sys

argc = len(sys.argv)
if argc == 2:
  n = int(sys.argv[1])
  if (n >= 0):
    summorial = 0
    while n > 0:
      summorial += n
      n -= 1
    print(summorial)
  else:
    print("Error! n must be >=0")
else:
  print("Error! Usage: python3 ft_summorial.py <n>")