import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD

def GetAllBook():
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM "Book" ')
    print(cursor.fetchall())
    cursor.close()

def GetAllAuthor():
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Author ')
    print(cursor.fetchall())
    cursor.close()

