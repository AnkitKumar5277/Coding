import math

def calculate_area_of_circle(radius):
    """Return the area of a circle given the radius."""
    return math.pi * radius ** 2
class Circle:
    """Class to represent a circle."""
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2
if __name__ == "__main__":
    circle = Circle(5)
    print("Circle Area:", circle.area())
    print("Area using function:", calculate_area_of_circle(5))
