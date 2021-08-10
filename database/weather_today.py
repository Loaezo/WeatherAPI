import requests
import json
from datetime import datetime
import time

from ranges.wind_strength import wind_description
from ranges.compass import wind_direction

api_key = '1508a9a4840a5574c822d70ca2132032'
# api_key = 'e59787e474f33127ab82d3d07a47ba33'
city = 'la plata'
country_abbreviated = 'ar'
url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric' \
    .format(city, country_abbreviated, api_key)
response = requests.get(url)
data = json.loads(response.text)

location_name = data['name'] + ', ' + data['sys']['country']

temperature_celsius_float = round(data['main']['temp'], 2)
temperature_celsius = str(temperature_celsius_float) + ' °C'

temperature_farenheit_float = round((data['main']['temp']) * 9 / 5 + 32, 2)
temperature_farenheit = str(temperature_farenheit_float) + ' °F'

wind_speed = data['wind']['speed']
wind_degrees = data['wind']['deg']
wind = str(wind_description(round(wind_speed * 100, 2))) + ', ' \
       + str(wind_speed) + ' m/s, ' \
       + wind_direction(wind_degrees)

cloudiness = data['weather'][0]['description']

pressure = str(data['main']['pressure']) + ' hPa'

humidity = str(data['main']['humidity']) + '%'

sunrise_epoch = data['sys']['sunrise']
sunrise = datetime.fromtimestamp(sunrise_epoch).strftime('%c')[11:19]

sunset_epoch = data['sys']['sunset']
sunset = datetime.fromtimestamp(sunset_epoch).strftime('%c')[11:19]

longitude = str(round(data['coord']['lon'], 2))
latitude = str(round(data['coord']['lat'], 2))
geo_coordinates = '[' + longitude + ' ' + latitude + ']'


epoch_now = time.time()
requested_time = str(datetime.now())[:19]
print(wind)