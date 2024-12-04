class Circle:
    # コードが期待通り動作するように実装
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.1415
        return round(self.radius * self.radius * pi, 2)

    def perimeter(self):
        pi = 3.1415
        return round(self.radius * 2 * pi, 2)


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
