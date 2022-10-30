"""
Will Bohmann
From Week 8 -
To earn a starting position on the wrestling team, a player must meet at least one of the following conditions:
    His weight is equal to or more than 150 and less than 160, and he has won 5 or more matches
    His weight is more than 199, or his number of wins is greater than 20
Write a program starter.py that asks for input of two values, weight which is a float
representing a player’s weight and numWins which is an int representing the number of wins the player has had.
The program should print out an appropriate message stating whether or not the individual should start.
"""



def starter():
    print("Let's see if your wrestler can start:")
    weight = int(input("What is the wrestler's weight? "))
    numWins = int(input("How many matches has your wrestler won?: "))
    if weight >=150 and weight < 160 and numWins >=5:
        print("This wrestler is a starter!")
    elif weight > 199 or numWins > 20:
        print("This wrestler is a starter!")
    else:
        print("Sorry, this wrestler cannot start")
    
starter()
