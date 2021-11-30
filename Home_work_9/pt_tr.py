class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __rsub__(self, other):
        self.x = other.x - self.x
        self.y = other.y - self.y
        return self

    def getx(self):
        return self.x

    def gety(self):
        return self.y


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


a1 = Point(1, 2)
b1 = Point(5, 6)
c1 = Point(3, 9)

t = Triangle(a1, b1, c1)


def perimeter(self):
    self.ab = 0.5 * ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
    self.bc = 0.5 * ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
    self.ac = 0.5 * ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
    return self.ab + self.bc + self.ac


def area(self):
    semi_per = self.perimeter() / 2
    return 0.5 * (semi_per * (semi_per - self.ab) * (semi_per - self.bc) * (semi_per - self.ca))


def __getnewargs__(self):
    return [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]


print(a1.x, b1.x, c1.x)
print(a1.y, b1.y, c1.y)
print(a1.getx())
print(b1.gety())
print(dir(t))
