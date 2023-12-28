import sys

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"

class Circle:
  def __init__(self, point, radius):
    self.center = Point(point[0], point[1])
    self.radius = radius
  
  def __str__(self):
    return f"Circle of center {self.center} and radius {self.radius}"
  
  def contains(self, point):
    return (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 <= self.radius ** 2

if __name__ == "__main__":
  argc = len(sys.argv)
  if argc == 3:
    circle = Circle((0, 0), 1)
    point = Point(float(sys.argv[1]), float(sys.argv[2]))
    if circle.contains(point):
      result = "in"
    else:
      result = "out"
    print(f"The Point {point}, lies {result} of the {circle}")
  else:
    print("Error! Usage: python3 circle.py <point.x> <point.y>")
