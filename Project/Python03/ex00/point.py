import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
def distance(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

if __name__ == "__main__":
  coord1 = input("Insert the coordinates of the first point: ").split(",")
  coord2 = input("Insert the coordinates of the second point: ").split(",")
  p1 = Point(eval(coord1[0]), eval(coord1[1]))
  p2 = Point(eval(coord2[0]), eval(coord2[1]))
  print(f"Their distance is: {distance(p1, p2)}")
