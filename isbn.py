"""
Week 8 - Will Bohmann
Write isbn.py that asks the user to input an ISBN. (Note: Read the number as a string.)
The program should then calculate the sum of the digits using the formula mentioned above and determine if the ISBN is a valid number. 
"""

def isbn():
    isbnNum = input("Please list the isbn number of your book: ")
    total = 0 #accumulator
    for i in range(len(isbnNum)): # iterates from 0 to the length of the string (minus 1)
        n = isbnNum[i]            # the ith character in the string
        num = int(n)           # convert to an integer
        total += (i+1) * num   # sum the digit times the increment
    d10 = total % 11           # mod 11
    if d10 == 0:
        print("Your ISBN number is valid")
    else:
        print("Your ISBN number is not valid")
    

isbn()
