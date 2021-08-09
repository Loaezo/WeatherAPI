from fastapi import FastAPI
from fastapi.responses import JSONResponse

from database.database import database_connection
from database.models import Weather
from database.models import save_weather_information

app = FastAPI(title='Weather API',
              description='Tech evaluation for Globant <3')


@app.get("/weather", response_class=JSONResponse)
async def get_weather(city: str, country: str):
    try:
        headers = {'content-type': 'application/json'}
        if len(country) == 2:
            save_weather_information()
            content = {"city": city,
                       "country": country}
            return JSONResponse(content=content, headers=headers)

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