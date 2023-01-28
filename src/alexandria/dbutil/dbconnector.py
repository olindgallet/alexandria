# Author: Olin Gallet
# Date: 26/1/2022
#
# The DBConnector loads up parameters from the environment and provides connection
# to the postgreSQL server.

import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DBConnector:
    def __init__(self, db:str='postgres'):
        self._connector = psycopg2.connect(user=os.environ['PGUSER'], database=db, host=os.environ['PGHOST'], password=os.environ['PGPASSWORD'])
        self._connector.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    def get_cursor(self):
        ''' Gets a cursor for this connector
        '''
        return self._connector.cursor()

    def close(self):
        ''' Closes the connection.
        '''
        self._connector.close()
    
    def commit(self):
        self._connector.commit()