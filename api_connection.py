import requests
import json

api_key = '1508a9a4840a5574c822d70ca2132032'
# api_key = 'e59787e474f33127ab82d3d07a47ba33'
city = 'Bogota'
country_abbreviated = 'co'
url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric'.format(city, country_abbreviated, api_key)

response = requests.get(url)
data = json.loads(response.text)
location_name = data['name'] + ',' + data['sys']['country']
temperature_celsius = str(data['main']['temp']) + '°C'
temperature_farenheit = str(data['main']['temp']) + '°C'

print(type(temperature_celsius))
print(temperature_celsius)
