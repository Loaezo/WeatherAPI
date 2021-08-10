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


def save_weather_information(city='la plata', country='ar'):
    weather_object = Weather(location_name=consume_api(city, country)[0],
                             temperature_celsius=consume_api(city, country)[1],
                             temperature_farenheit=consume_api(city, country)[2],
                             wind=consume_api(city, country)[3], cloudiness=consume_api(city, country)[4],
                             pressure=consume_api(city, country)[5], humidity=consume_api(city, country)[6],
                             sunrise=consume_api(city, country)[7], sunset=consume_api(city, country)[8],
                             geo_coordinates=consume_api(city, country)[9])
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


def get_weather_field():
    return Weather.select(Weather.requested_time).where(Weather.id == 1)