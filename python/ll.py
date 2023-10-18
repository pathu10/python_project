# To caluclate perimeter of circle, square, rectangle,triangle

print("Welcome to area caluclator")
print("Select the area that you want to caluclate")
print("To find perimter of Circle, type = circle()")
print("To find perimter of Square, type = square()")
print("To find perimter of Rectangle, type = rectangle()")
print("To find perimter of Triangle, type = triangle()")

def circle():
    PI= 3.1415927
    r=float(input("Enter the radius: "))
    P=2*PI*r
    print("Perimter=%0.3f"%P)
    
def square():
    a=float(input("Enter the lenght of side: "))
    P=4*a
    print("Perimter=",P)

def rectangle():
    a=float(input("Enter the lenght of sides1: "))
    b=float(input("Enter the lenght of sides2: "))
    P=2*(a+b)
    print("Perimter=",P)

def triangle():
    a=float(input("Enter the value of side1: "))
    b=float(input("Enter the value of side2: "))
    c=float(input("Enter the value of side3: "))
    P=a+b+c
    print("Perimter=",P)



