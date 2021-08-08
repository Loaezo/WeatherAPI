import requests
import json

"""
Returns the daily forecast as given by openweathermap.org
"""
api_key = '1508a9a4840a5574c822d70ca2132032'  # test api key, given by an example
# api_key = 'e59787e474f33127ab82d3d07a47ba33' # actual api key, given when registered to openweatherapi.org
city = 'London'
country_abbreviated = 'gb'
url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}&appid={}&units=metric' \
    .format(city, country_abbreviated, api_key)

response = requests.get(url)
data = json.loads(response.text)

forecast = data['list'][1:3]

print(forecast)