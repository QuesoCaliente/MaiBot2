import psycopg2
import sys, os
from pprint import pprint
from decouple import config


class DataBaseConexion:
    def __init__(self):
        try:
            databaseurl = config('DATABASE_URL')
            self.conexion = psycopg2.connect(databaseurl)
            self.conexion.autocommit = True
            self.cursor = self.conexion.cursor()
        except Exception as err:
            pprint(f'No ha sido posible la conexion {err}')
            print(sys.exc_info())

