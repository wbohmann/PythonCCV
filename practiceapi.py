#api practice - Will
#December 2, 2022

#importing libraries
import requests
import json
print("This is a small program can look up UPC codes from a upc database using an API")
print("")
print("If you need a sample to try, use this number: 889842018752 or find your own")

upcode =input("Please input your UPC code, it is 12 numbers: ")
baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': upcode}
response = requests.get(baseURL,params=parameters)
#print(response.url)
content = response.content
info = json.loads(content)
#print(type(info))
#print(info) 

item=info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
lowPrice =itemInfo['lowest_recorded_price']
highPrice = itemInfo['highest_recorded_price']
print("____________")
print("Product: ",title, "Brand: ",brand, "Low Price: ",lowPrice, "High Price: ",highPrice, sep='\n')


#instruction from this code came from LinkedIn Learning Course Using Python for Automation
