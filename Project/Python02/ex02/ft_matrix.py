import sys

argc = len(sys.argv)
if argc == 3:
  columns = int(sys.argv[1])
  rows = int(sys.argv[2])

  matrix = [[float(input(f"Insert the element in position {y} {x}: ")) for x in range(rows)] for y in range(columns)]
  for y in range(columns): 
    print(matrix[y])

  sum_row = 0
  sum_rows = []
  for y in range(columns):
    sum_row = 0
    for x in range(rows):
      sum_row += matrix[y][x]
    sum_rows.append(sum_row)
  print("The sum over rows is:")
  print(sum_rows)
    
  sum_column = 0
  sum_columns = []
  for x in range(rows):
    sum_column = 0
    for y in range(columns):
      sum_column += matrix[y][x]
    sum_columns.append(sum_column)
  print("The sum over columns is:")
  print(sum_columns)
else:
  print("Error! Usage: python3 ft_matrix.py <n> <m>")