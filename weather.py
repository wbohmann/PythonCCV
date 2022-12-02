#Making an API for weather
#Will Bohmann 
#December 2, 2022

import requests
import json

baseURL = 'https://api.openweathermap.org/data/2.5/weather'
parameters = {'appid': '9d3c2f95a643573b920cb35c3db262a1', 'q':'Jericho,US'}
response = requests.get(baseURL, parameters)

content = response.content
info = json.loads(content) #json takes the date and breaks up into dictionaries
print(type(info))
print(info)

weather=info["description"]
temperature = main['temp']
weatherInfo =item[0]
temperatureMain = main[0]

forecast =weatherInfo["description"]
pizza = temperatureMain["temp"]
print(forecast, pizza, sep='\n')


