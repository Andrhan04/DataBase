import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os

def InsertInstance(book_id,place_id):
    #   25.09.2024
    #Вставка новой связи
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Instance(book_id,place_id) VALUES (%s,%s)',(book_id,place_id))
    connectBD.conn.commit()
    cursor.close()

def InsertAuthor(FIO):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Author(FIO) VALUES (%s)',(FIO,))
    connectBD.conn.commit()
    cursor.close()

def InsertBook(name,Description):
    #   19.09.2024
    #вставка новой книги   - не сделано?
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Book (name,Description) VALUES (%s,%s)',(name,Description))
    connectBD.conn.commit()
    cursor.close()

def InsertBook_Depository(name,place ):
    #   20.09.2024
    #вставка нового книгохранилища - не сделано?
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Book_Depository (name,place) VALUES (%s,%s)',(name,place))
    connectBD.conn.commit()
    cursor.close()

def InsertBookAuthor(book,author ):
    #   20.09.2024
    #вставка новой связи между автором и книгой - не сделано? 
    cursor = connectBD.conn.cursor()
    cursor.execute('INSERT INTO Book_Author (book_id, author_id) VALUES (%s,%s)',(book,author))
    connectBD.conn.commit()
    cursor.close()


def Create():
    # 19.09.2024
    # создание таблиц (на данный момент не работает, возвращает Строку ничего) 
    cursor = connectBD.conn.cursor()
    cursor.execute('CREATE TABLE Book (id SERIAL PRIMARY KEY, name TEXT, Description TEXT)')
    connectBD.conn.commit()
    cursor.close()
    return "Nothing"