
import math

print("WELCOME TO MY AREA CALCULATOR")

# Circle, Square, Rectangle, Triangle

print("")

print("Choose your shape")
print("Circle")
print("Square")
print("Rectangle")
print("Triangle")

print("")

answer = input("Choose what shape u wanna calculate C/S/R/T: ").upper()

if answer == "C":
    radius = float(input("Enter Radius: "))
    area = math.pi * radius ** 2
    print("The area of circle is: " , area)

elif answer == "S":
    sidelength = (float("Enter sidelength: "))
    area = side ** 2
    print("The area of the square is: " , area)

elif answer == "R":
    length = (float("Enter length: "))
    width = (float("Enter width: "))
    area = length * width
    print("The area of the rectangle is: " , area)

elif answer == "T":
    base = (float("Enter length: "))
    height = (float("Enter height: "))
    area = (base * height) / 2
    print("The are of the triangle is: " , area)

else:
    print("Invalid choice")