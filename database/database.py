import peewee

database_connection = peewee.MySQLDatabase(
    'fastapi',
    user='admin',
    password='Welcome1!',
    host='fastapi.c1lrgmovngsy.us-east-2.rds.amazonaws.com',
    port=3306
)


