#December 2, 2022
#Will Bohmann
#importing libraries

from tkinter import *
from tkinter import ttk
import requests
import json

#print("This is a small program can look up UPC codes from a upc database using an API")
#print("")
#print("If you need a sample to try, use this number: 889842018752 or find your own")


#Tkinter Interface   
root = Tk()
entry = ttk.Entry(root, width = 30)
entry.pack()


label = ttk.Label(root, text = "Enter a UPC Code")
label.pack()
label = ttk.Label(root, text = "Try: 889842018752 or find your own")
label.pack()
label.config(foreground = 'blue', background = 'yellow')
label.config(font = ('Courier', 18, 'bold'))
button = ttk.Button(root, text = "Enter")
button.pack()
#button.config(command = callback)

#upcode =input("Please input your UPC code, it is 12 numbers: ")
def upc():
    upcode =input()
    baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'         #we want the base url infront of the question mark
    parameters = {'upc': upcode}  #this is a python dicstionary  upc is the key and the barcode is the value, I made a varible for the barcode so that a user can enter a barcode
    response = requests.get(baseURL,params=parameters)
    #print(response.url)  You can use this print to test your API request

    #managing the reponses from the website's interface.  To make the response more navigable, use json
    content = response.content
    info = json.loads(content) #the loads from json makes the information more friendly

    #First we need to hone in on the items key in the dictionary as this contains the brand and name information
    item=info['items']
    itemInfo = item[0]
    title = itemInfo['title'] 
    brand = itemInfo['brand']
    lowPrice =itemInfo['lowest_recorded_price']
    highPrice = itemInfo['highest_recorded_price']
    print("____________")
    print("Product: ",title, "Brand: ",brand, "Low Price: ",lowPrice, "High Price: ",highPrice, sep='\n')



def callback():
    upc()

button.config(command = callback)
root.mainloop()



