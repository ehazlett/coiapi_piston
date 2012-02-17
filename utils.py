from pymongo import Connection
from django.conf import settings

def get_mongodb_connection():
    conn = Connection(settings.MONGODB_HOST, settings.MONGODB_PORT)
    return conn
