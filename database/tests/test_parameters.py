import requests
import json
from database import weather_today
from ranges.wind_strength import wind_description
from ranges.compass import wind_direction
from datetime import datetime


def test_api_format_is_correct():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,gb&appid=e59787e474f33127ab82d3d07a47ba33&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    temperature_celsius_float = round(data['main']['temp'], 2)
    temperature_celsius = str(temperature_celsius_float) + ' °C'
    temperature_farenheit_float = round((data['main']['temp']) * 9 / 5 + 32, 2)
    temperature_farenheit = str(temperature_farenheit_float) + ' °F'
    wind_speed = data['wind']['speed']
    wind_degrees = data['wind']['deg']
    wind = str(wind_description(round(wind_speed * 100, 2))) + ', ' + str(wind_speed) + ' m/s, ' \
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

    assert weather_today.consume_api('London', 'gb') == ('London, GB',
                                                         temperature_celsius,
                                                         temperature_farenheit,
                                                         wind, cloudiness, pressure,
                                                         humidity, sunrise, sunset,
                                                         geo_coordinates)