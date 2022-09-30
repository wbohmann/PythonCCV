# RectangleArea.py
# William Bohmann
# This program calucates the area of a rectangle
# function definition below

def rectangleArea():
    print("I am going to show you the power of Python...")
    print("Let's start by showing you the area of a rectangle")
    length = int(input("Enter the length, whole numbers please: "))
    width = int(input("Enter the width: "))
    area = length*width
    print("The area of this rectangle = " + str(area))

rectangleArea()
