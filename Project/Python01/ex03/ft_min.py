import sys

def my_min(n1=0,n2=0,n3=0):
  min = n1
  for n in [n1,n2,n3]:
    if n < min:
      min = n
  return min
  
if __name__ == "__main__":
  argc = len(sys.argv)
  if argc == 4:
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
    n3 = float(sys.argv[3])
    print(f"The min is: {my_min(n1,n2,n3)}")
  else:
    print("Error! Usage: python3 ft_min.py <x> <y> <z>")