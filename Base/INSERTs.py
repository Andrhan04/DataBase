import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD

def Create():
    cursor = connectBD.conn.cursor()
    cursor.execute('CREATE TABLE Author (id SERIAL PRIMARY KEY FIO TEXT)')
    cursor.commit()
    cursor.close()

def InsertAuthor(id,FIO):
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Author(FIO) VALUES (%s)RETURNING id',(FIO))
    cursor.commit()
    print(cursor.fetchall())
    cursor.close()
