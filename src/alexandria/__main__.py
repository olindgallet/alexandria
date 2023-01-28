#!/usr/bin/env python3

# Author: Olin Gallet
# Date:  24/1/2023
import sys

from .dbutil.dbconnector import DBConnector
from .dbutil.createdbcommand import CreateDBCommand
from .dbutil.createtablecommand import CreateTableCommand
from .dbutil.insertrecordcommand import InsertRecordCommand

def execute():
    connector = DBConnector('alexandria')
    cursor = connector.get_cursor()
    #CreateTableCommand('movies').execute(cursor)
    InsertRecordCommand('movies', 'Suspiria').execute(cursor)
    cursor.close()
    connector.close()
    #cur.execute("SELECT * FROM pg_database;")
    #cur.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\';')
    #cur.close()
    #con.close()
    
if __name__ == '__main__':
    execute()