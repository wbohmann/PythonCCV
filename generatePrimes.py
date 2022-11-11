'''
Will Bohmann
Week 10
A prime number is any number greater than 1.
They only have two factors, 1 and the number itself. This means these numbers cannot be divided by any number other than 1 and the number itself
Write a program called generatePrimes.py that prompts the user for a number n and outputs all the primes less than or equal to n. 

For example, if we wished to find all the primes up to 10, the list would originally contain [2, 3, 4, 5, 6, 7, 8, 9, 10].  The 2 is removed and announced to be prime.  Then 4, 6, 8, and 10 are removed, since they are multiples of 2.  That leaves [3, 5, 7, 9].  Repeating the process, 3 is announced as prime, and 9 is removed because it is a multiple of 9.  That leaves [5, 7].  And so on.

A youtube example that helps show this work  https://www.youtube.com/watch?v=-wIYdmPiHcA
'''
#when you import the math module, you can return the square root of a number.  We want to do that in this program.

import math

n = int(input("Give me a number to run this program: "))    #this is our user imput to find the length of the array we should evaluate
primes = [2]                                                #this creates an array called prime with an item in it
numbertest = 3                                              #we need a number to compare against the number our user added.  Since 0,1 are not prime numbers 
while numbertest < n:                                       #for as long as 3 is less than the user number, iterate the following:
    i = 0                                                   #initialize a variable to run through the loop
    while primes[i] <= math.sqrt(numbertest):               #all numbers divisible by 2 or greater than or equal to the square root of the prime will be not be prime
        if (numbertest % primes[i]) == 0:                   #this is the modulus with finds the remainder if the remainder is equal to zero, add
            numbertest += 1
            break
        else:
            i += 1
    else:                                                   #the while loop begins if the first check is less than the square root of the numbertest, append the number test variable and add the next instance
        primes.append(numbertest)
        numbertest += 1
print(primes)


