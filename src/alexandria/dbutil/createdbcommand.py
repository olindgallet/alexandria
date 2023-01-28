# Author: Olin Gallet
# Date: 26/1/2023
#
# The MakeDBCommand is used to make a database in the postgreSQL ecostystem.
# 
from .dbcommand import DBCommand

class CreateDBCommand(DBCommand):
    def __init__(self):
        pass

    def execute(self, cursor):
        ''' Creates a new Alexandria database.
        '''
        cursor.execute('DROP DATABASE IF EXISTS alexandria')
        cursor.execute('CREATE DATABASE alexandria')

    