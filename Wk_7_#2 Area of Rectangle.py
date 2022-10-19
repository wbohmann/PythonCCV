2.  #write a function for area of rectangle
#Area of a rectangle is width * height

    
def areaRect():
    length = int(input("Give me a length of one side "))
    width = int(input("Give me the width of another side "))
    area = length*width
    print("The area of your rectangle is: " + str(area))
    
areaRect()
