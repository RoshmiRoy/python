class rect:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width


    def __lt__(self, other):
        a1 = self.__length * self.__width
        a2 = other.__length * other.__width
        if a1 < a2:
            print("The greater is the second one")
        else:
            print("The greter is the first one")
wid1 = int(input("Enter bredth of First Rectangle:"))
leng2 = int(input("Enter length of Second Rectangle:"))
wid2 = int(input("Enter bredth of Second rectangle:"))
leng1= int(input("Enter bredth of First Rectangle:"))
rect1 = rect(leng1, wid1)
rect2 = rect(leng2, wid2)
print("FIRST RECTANGLE\n")
rect1.area()
print("\nSECOND RECTANGLE\n")
rect2.area()
print(rect1 < rect2)