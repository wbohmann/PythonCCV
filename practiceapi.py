#api practice - Will
#December 2, 2022

#importing libraries
import requests
import json

baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '889842018752'}
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
print(title, brand, lowPrice, highPrice, sep='\n')


#instruction from this code came from LinkedIn Learning Course Using Python for Automation
