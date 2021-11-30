class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __rsub__(self, other):  # rsub (а не sub) т.к. правосторонняя операция)
        self.x = other.x - self.x
        self.y = other.y - self.y
        return self

#   def Show(self, text):  - метод выводит точку
#       print(text, " = (", self.x, "; ", self.y, ")")

    def getx(self):
        return self.x

    def gety(self):
        return self.y


#   def getXY(self):  - метод возвращает в виде списка (x, y)
#        return [self.x, self.y]


pt1 = Point(0, 0)
pt2 = Point(6, 7)
pt3 = Point(3, 4)


"""class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, ab, bc, ac):
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = x1, y1, x2, y2, x3, y3
        self.ab = ab
        self.bc = bc
        self.ac = ac
        self.perimeter = 0
        self.area = 0

    def perimeter(self):
        self.ab = 0.5 * ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.bc = 0.5 * ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.ac = 0.5 * ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        res = self.ab + self.bc + self.ac
        return res

    def area(self):
        semi_per = self.ab + self.bc + self.ac / 2
        return 0.5 * (semi_per * (semi_per - self.ab) * (semi_per - self.bc) * (semi_per - self.ac))

    def __getnewargs__(self):
        return [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]


print(pt1.x, pt2.x, pt3.x)
print(pt1.y, pt2.y, pt3.y)
print(pt1.getx())
print(pt2.gety())"""


class Triangle:
    def __init__(self, a, b, c):

        def sideLen(p1, p2):
            return 0.5 * ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        self.a = a
        self.b = b
        self.c = c
        self.ab = sideLen(self.a, self.b)
        self.bc = sideLen(self.b, self.c)
        self.ca = sideLen(self.c, self.a)

    def perimeter(self):
        return self.ab + self.bc + self.ca

    def area(self):
        semi_perimeter = self.perimeter() / 2
        return 0.5 * (semi_perimeter * (semi_perimeter - self.ab) * (semi_perimeter - self.bc) *
                      (semi_perimeter - self.ca))


tr1 = Triangle((-3, 2), (5, 7), (-2, 1))

print(pt1.x, pt2.x, pt3.x)
print(pt1.y, pt2.y, pt3.y)
print(pt1.getx())
print(pt2.gety())
print(tr1.perimeter())
print(tr1.area())
