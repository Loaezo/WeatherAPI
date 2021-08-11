import requests
import json

from pydantic import BaseSettings
from datetime import datetime

from ranges.wind_strength import wind_description
from ranges.compass import wind_direction


class Settings(BaseSettings):
    api_key: str


settings = Settings()


def consume_api(city_1, country_1):
    """
    Function that evaluates the data returned from openweathermap.org
    and converts the information in the requested format
    :param city_1: The city from where you want the current weather
    :param country_1: The country the city belongs to, this is to prevent ambiguous results,
                    as there are many cities with the same name
    :return: The fields that are to be saved in the database in the required format
    """
    api_key = settings.api_key

    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units=metric' \
        .format(city_1, country_1, api_key)
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

    return location_name, temperature_celsius, \
           temperature_farenheit, wind, cloudiness, \
           pressure, humidity, sunrise, sunset, geo_coordinates
