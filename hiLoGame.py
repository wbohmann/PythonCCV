"""
Lab07 Random Number Game
Will Bohmann
"""

#generate a random number, so use import random library, 7 guesses
import random
x=random.randint(1,100)
attempts = 0
while attempts <7:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts +=1
    if guess < x:
        print("your guess is too low")
    if guess > x:
        print("your guess is too high")
    if guess == x:
        print("your guess is correct!, the number is", x ,"You win in", attempts, "guesses")
        break
else:
    print("You did not guess the number, the number was: " + str(x))
