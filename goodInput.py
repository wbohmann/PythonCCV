"""
Lab7/Week 9
Will Bohmann
Use While loop and find a number in a range
"""
import random
x=random.randrange(1,10)

while x:
    guess =int(input("Guess a number: "))
    if guess <x:
        print("Sorry your guess is out of range and too low, give it another go")
    if guess >x:
        print("Sorry your guess is out of range and too high, give it another go")
    if guess ==x:
        print("Congratulations, you got the number correct.  My secret number was " +str(x))
        break
        

    
    
