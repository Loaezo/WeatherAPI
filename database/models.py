import peewee
import datetime

from pydantic.utils import GetterDict
from typing import Any
from database import weather_today
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


def save_weather_information():
    weather_object = Weather(location_name=weather_today.location_name,
                             temperature_celsius=weather_today.temperature_celsius,
                             temperature_farenheit=weather_today.temperature_farenheit,
                             wind=weather_today.wind, cloudiness=weather_today.cloudiness,
                             pressure=weather_today.pressure, humidity=weather_today.humidity,
                             sunrise=weather_today.sunrise, sunset=weather_today.sunset,
                             geo_coordinates=weather_today.geo_coordinates)
    weather_object.save()
    return weather_object


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class WeatherModel(BaseModel):
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
    return Weather.select().where(Weather.id == 1).dicts().get()
