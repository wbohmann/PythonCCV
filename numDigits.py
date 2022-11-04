"""
Lab7/Week 9
Will Bohmann
Use While loop count the number of digits
"""
number =int(input("Give me a number: "))
count = 0
while(number>0):
    count = count +1
    number=number//10
print("The number of digits in your number is: " ,count)

        

    
    
