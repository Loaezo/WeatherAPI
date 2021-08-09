from peewee import Model

from database.database import database_connection


class BaseModel(Model):
    class Meta:
        database = database_connection