import datetime

from datetime import timedelta

from fastapi import FastAPI
from fastapi.responses import JSONResponse


from database.database import database_connection
from database.models import Weather, get_weather_data, get_weather_field
from database.models import save_weather_information

app = FastAPI(title='Weather API',
              description='Tech evaluation for Globant <3')


@app.get("/weather", response_class=JSONResponse)
def get_weather(city: str, country: str):
    try:
        if len(country) == 2:
            if get_weather_field() - datetime.datetime.now() > timedelta(minutes=2):
                Weather.drop_table(Weather)
                database_connection.create_tables([Weather])
                save_weather_information(city, country)
                return get_weather_data()
            else:
                return get_weather_data()
        else:
            return {'ValueError: The country length should be 2 characters long'}
    except ValueError:
        print('The country length should be 2 characters long')


@app.on_event('startup')
def startup():
    if database_connection.is_closed():
        database_connection.connect()
    database_connection.create_tables([Weather])


@app.on_event('shutdown')
def shutdown():
    if not database_connection.is_closed():
        database_connection.close()