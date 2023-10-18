# To caluclate area of circle, square, rectangle,triangle,triangle(all side given)
print("Welcome to area caluclator")
print("Select the area that you want to caluclate")
print("To find area of Circle, type = circle()")
print("To find area of Square, type = square()")
print("To find area of Rectangle, type = rectangle()")
print("To find area of Triangle, type = triangle()")
print("To find area of Triangle when all sides are given, type = triangle_side()")

def circle():
    PI= 3.1415927
    r=float(input("Enter the radius: "))
    area=PI*r*r
    print("Area=%0.3f"%area)
    
def square():
    a=float(input("Enter the lenght of side: "))
    area=a*a
    print("Area=",area)

def rectangle():
    a=float(input("Enter the lenght of sides1: "))
    b=float(input("Enter the lenght of sides2: "))
    area=a*b
    print("Area=",area)

def triangle():
    h=float(input("Enter the value of height: "))
    b=float(input("Enter the value of base: "))
    area=h*b/2
    print("Area=",area)

def triangle_side():
    a=float(input("Enter the value of side1: "))
    b=float(input("Enter the value of side2: "))
    c=float(input("Enter the value of side3: "))
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area=%0.3f"%area)


