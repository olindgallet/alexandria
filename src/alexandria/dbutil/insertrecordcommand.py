# Author: Olin Gallet
# Date: 26/1/2023
#
# The InsertRecordCommand is used to make a table in the postgreSQL ecostystem.
# 
from .dbcommand import DBCommand
from psycopg2.sql import SQL, Identifier

class InsertRecordCommand(DBCommand):
    def __init__(self, table_name:str, media_name:str):
        self._table_name = table_name
        self._media_name = media_name

    def execute(self, cursor):
        ''' Creates a new table based on the parameters.
        '''
        #query = SQL("INSERT INTO {table}(name) VALUES ({media});").format(table = Identifier(self._table_name), media = Identifier(self._media_name))
        query = SQL("INSERT INTO movies(name) VALUES('Suspiria');")
        cursor.execute(query)

    