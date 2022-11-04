class Triangle():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a+self.b+self.c
a = int(input("Enter length of rectangle: "))
b = int(input("Enter width of rectangle: "))
c= int(input("Enter width of rectangle: "))
obj = Triangle(a, b,c)
print("Area of rectangle:", obj.perimeter())
