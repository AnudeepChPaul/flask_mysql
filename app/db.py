from mysql import connector

from config import DATABASE_CONNECT_OPTIONS

db = connector.connect(**DATABASE_CONNECT_OPTIONS)
