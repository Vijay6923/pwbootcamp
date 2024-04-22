import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_from_point(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        
        return math.sqrt(dx**2 + dy**2 )
    
    

point1 = Point(1,2)
point2 = Point(4,5)

print("Distance from origin:", point1.distance_from_origin())

print("Distance from point2:", point1.distance_from_point(point2))

