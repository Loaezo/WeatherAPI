from fastapi import FastAPI

from database.database import database as connection
from database.database import Weather

app = FastAPI(title='Weather API',
              description='Tech evaluation for Globant <3')


@app.get("/weather")
async def get_weather(city: str, country: str):
    return {"city": city,
            "country": country}


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([Weather])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()