import peewee

database_connection = peewee.MySQLDatabase(
    'fastapi',
    user='root',
    password='1',
    host='localhost',
    port=3306
)  # environment variables


