# Author: Olin Gallet
# Date: 26/1/2023
#
# The CreateTableCommand is used to make a table in the postgreSQL ecostystem.
# 
from .dbcommand import DBCommand
from psycopg2.sql import SQL, Identifier

class CreateTableCommand(DBCommand):
    def __init__(self, table_name:str):
        self._table_name = table_name

    def execute(self, cursor):
        ''' Creates a new table based on the parameters.
        '''
        query = SQL('CREATE TABLE IF NOT EXISTS {table} (' \
              'id SERIAL PRIMARY KEY,' \
              'name TEXT NOT NULL,' \
              'rating INT,' \
              'date_watched DATE,' \
              'review TEXT' \
              ');').format(table = Identifier(self._table_name))
        cursor.execute(query)

    