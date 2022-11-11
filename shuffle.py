#Will Bohmann
#Week 10
#Write a function to shuffle a list
    
def shuffle():
    import random                                         #imports the random library module
    n = input("Enter a list of ingredients with spaces:") #stores variable of user input
    list1 = n.split()                                     #splits the input into a list
    x = len(list1)                                        #determines the lenght of the list
    random.shuffle(list1)                                 #takes the list and shuffles
    print("That's " + str(x) + " Ingredients.\nYour list of ingredients shuffled " + str(list1[0:])) 
                                                          #prints the list range from position zero to the end of the list
    
shuffle()
