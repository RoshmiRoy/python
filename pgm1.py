class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def per(self):
         return 2*(self.length + self.breadth)
print("rectangle 1")
a = int(input("enter the length"))
b = int(input("enter the breadth"))
rect1 = rectangle(a,b)
print("Area 1 = ",rect1.area())
print("Perimeter = ",rect1.per())
print("rectangle 2")
a = int(input("enter the length"))
b = int(input("enter the breadth"))
rect2 = rectangle(a, b)
print("Area 1 = ",rect2.area())
if rect1.area() == rect2.area():
    print("both area are same")
else:
    print("both area are different")