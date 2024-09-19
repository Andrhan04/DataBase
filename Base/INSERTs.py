import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD

def Create():
    cursor = connectBD.conn.cursor()
    cursor.execute('CREATE TABLE Book_Depository (id SERIAL PRIMARY KEY, name TEXT, place TEXT)')
    connectBD.conn.commit()
    cursor.close()

def InsertAuthor(FIO):
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Author(FIO) VALUES (%s)',(FIO,))
    connectBD.conn.commit()
    cursor.close()

