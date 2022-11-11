#Will Bohmann
#Week 10
#Write and test a function called removeDuplicates(someList) that removes duplicate values from a list.
#if we have a list of numbers, look through that list and take out duplicates and append to a new list
#tutorial that helped explain:  https://www.youtube.com/watch?v=j6aHCZIMLa8

#list of numbers
data =[8, 17, 23, 43, 23, 8, 9, 11, 2, 17, 4, 6, 3] 

def removeDuplicates(someList):       #is a name of function with a parameter
    nodplist =[]                      #creating a variable for an empty list to hold the no duplicates
    for elements in someList:         #to go through each element in someList parameter we make a for loop
        if elements not in nodplist:
            nodplist.append(elements) #add the unique elements to the nodplist variable
    print("Your Original list: " + str(data))
    print ("Your list without duplicates: " +str(nodplist))

removeDuplicates(data)                #the data is the argument we are passing

#the function removeDuplicates will return a list called nodplist as the new list without duplicates
