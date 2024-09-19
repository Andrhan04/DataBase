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

def InsertBook(FIO):
    #вставка новой книги
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO "Author" () VALUES (%s)',(FIO,))
    connectBD.conn.commit()
    cursor.close()