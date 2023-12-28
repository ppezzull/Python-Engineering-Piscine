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

if __name__ == "__main__":
  circle = Circle((150, 100), 75)
  print(circle)
