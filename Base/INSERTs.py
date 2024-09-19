import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD

def InsertAuthor(FIO):
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Author(FIO) VALUES (%s)',(FIO,))
    connectBD.conn.commit()
    cursor.close()

def InsertBook(name, ):
    #вставка новой книги   - не сделано
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Book () VALUES (%s)',(name,))
    connectBD.conn.commit()
    cursor.close()

def Create():
    cursor = connectBD.conn.cursor()
    #cursor.execute('CREATE TABLE Book (id SERIAL PRIMARY KEY, name TEXT, Description TEXT, place_id int)')
    connectBD.conn.commit()
    cursor.close()
    return "Nothing"