from peewee import Model

from database.database import database_connection


class BaseModel(Model):
    """
    Class that declares the base model and the database connection
    """
    class Meta:
        database = database_connection