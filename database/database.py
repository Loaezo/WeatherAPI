import peewee

database = peewee.MySQLDatabase(
    'fastapi',
    user='root',
    password='1',
    host='localhost',
    port=3306
)  # environment variables


class Weather(peewee.Model):
    location_name = peewee.CharField(max_length=64)
    temperature_celsius = peewee.SmallIntegerField()
    temperature_farenheit = peewee.SmallIntegerField()
    wind = peewee.CharField(max_length=255)
    cloudiness = peewee.CharField(max_length=128)
    pressure = peewee.SmallIntegerField()
    humidity = peewee.SmallIntegerField()
    sunrise = peewee.SmallIntegerField()
    sunset = peewee.SmallIntegerField()
    geo_coordinates = peewee.CharField(max_length=64)
    requested_time = peewee.DateTimeField()

    def __str__(self):
        return 'Weather'

    class Meta:
        database = database
        table_name = 'Weather'
