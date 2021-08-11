import peewee
import datetime

from pydantic.utils import GetterDict
from typing import Any
from database.weather_today import consume_api
from database.database import database_connection
from database.base import BaseModel


class Weather(BaseModel):
    """
    Fields that are currently saved in the database using Peewee
    """
    location_name = peewee.CharField(max_length=64)
    temperature_celsius = peewee.CharField()
    temperature_farenheit = peewee.CharField()
    wind = peewee.CharField(max_length=255)
    cloudiness = peewee.CharField(max_length=128)
    pressure = peewee.CharField()
    humidity = peewee.CharField()
    sunrise = peewee.CharField()
    sunset = peewee.CharField()
    geo_coordinates = peewee.CharField(max_length=64)
    requested_time = peewee.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return 'Weather'

    class Meta:
        database = database_connection
        db_table = 'weather'
        table_name = 'Weather'


def save_weather_information(country, city):
    """
    Saves the data to the database taking two parameters
    :param country: Country from where you want the weather. This is to avoid confusion,
                    as there are multiple cities with the same name
    :param city: City you want the weather from
    :return: the weather object queried from the database
    """
    weather_object = Weather(location_name=consume_api(country, city)[0],
                             temperature_celsius=consume_api(country, city)[1],
                             temperature_farenheit=consume_api(country, city)[2],
                             wind=consume_api(country, city)[3], cloudiness=consume_api(country, city)[4],
                             pressure=consume_api(country, city)[5], humidity=consume_api(country, city)[6],
                             sunrise=consume_api(country, city)[7], sunset=consume_api(country, city)[8],
                             geo_coordinates=consume_api(country, city)[9])
    weather_object.save()
    return weather_object


class PeeweeGetterDict(GetterDict):
    """
    Function to be able to make queries using Peewee
    """
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class WeatherModel(BaseModel):
    """
    Weather model class to declare the type of the fields that will be saved in the database
    """
    id: int
    location_name: str
    temperature_celsius: str
    temperature_farenheit: str
    wind: str
    cloudiness: str
    pressure: str
    humidity: str
    sunrise: str
    sunset: str
    geo_coordinates: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


def get_weather_data():
    """
    Function that queries the first row in the database
    :return: the fields in the first row without the id
    """
    fields = [Weather.location_name, Weather.temperature_celsius, Weather.temperature_farenheit,
              Weather.wind, Weather.cloudiness, Weather.pressure, Weather.humidity, Weather.sunrise,
              Weather.sunset, Weather.geo_coordinates, Weather.requested_time]
    return Weather.select(*fields).where(Weather.id == 1).dicts().get()


def get_weather_field():
    """
    Function that queries the time at which the database field was created to compare it with a time delta
    :return: the date and time when the row was created
    """
    return Weather.select(Weather.requested_time).where(Weather.id == 1)