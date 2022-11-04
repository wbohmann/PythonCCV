"""
Lab 7 While Conditionals
Will Bohmann
Finding a number in a list

"""

#create a list
#ask user for number
#i is the variable that is set to 0 and will loop through the length of the list until it reaches the end
myList = [1,3,5,7,9,11,13,15,17,19]
number = int(input("Give me a number between 1 and 20: "))
i = 0
while i<len(myList):
    if myList[i] == number:  #if the list is equal to the number
        index = myList.index(number)
        print(myList[i], "Yes, that number is in the list")
        print("The first occurence of the number is position:", index, "in the list")
        break
    i+=1
else:
    print(number, "not found in list")
