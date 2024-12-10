# quiz/signalss.py

from django.db import connection
from django.db.backends.signals import connection_created

def set_timezone(sender, connection, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("SET timezone TO 'UTC';")

# Connect the signal to ensure it's called every time a database connection is made
connection_created.connect(set_timezone)
