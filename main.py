from fastapi import FastAPI

from database import database as connection
from database import Weather

app = FastAPI(title='Weather API',
              description='Tech evaluation for Globant <3')


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([Weather])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get("/weather/{city}{country}")
async def get_weather(city: str, country: str):
    return {"city": city,
            "country": country}