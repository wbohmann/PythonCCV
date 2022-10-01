def nameReverse():
    for x in range(3):
        name =input("How about a proper name: ")
        words = name.split()  #this will return a list
        print(words[1] + ", " + words[0])
        
nameReverse()

def companyName():
    for x in range(3):
        name =input("Enter a three part internet domain name, like www.Amazon.com: ")
        print(name[4:-4]) #in the range www. is the first four and -4 is last four
        
companyName()

def initials():
    num_range = int(input("How many names would you like to input?"))
    for x in range(num_range):
        f_name = input("Enter the first name of student: ")
        l_name = input("Enter the last name of student: ")
        print("The student's initials are "+ (f_name[0])+(l_name[0]))
    
initials()

def wordCount():
    for x in range(3):
        s = input("Write a short sentence: ")
        words = s.split() #this splits the sentance into a list
        number = len(words) #this counts the length of the list
        print (number)
    
wordCount()

def wordAverage():
    for x in range(3):
        s = input("Write a short sentence: ")
        number_letters = len(s) - s.count(" ") # counts lenght of sentence - spaces
        words = s.split() #this splits the sentance into a list
        number = len(words) #this counts the length of the list
        num_average =(number_letters / number)
        # make the total string size AT LEAST 10 (including digits and points), fill with zeros to the left
        print('{:0^10.2f}'.format(num_average))
       
wordAverage()
