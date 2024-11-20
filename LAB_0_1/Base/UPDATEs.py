import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os

def UpdateAuthor(id, FIO):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('UPDATE Author SET FIO = (%s) WHERE id = %s ',(FIO,id,))
    connectBD.conn.commit()
    cursor.close()

def UpdateBook(id, name, description):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    try:
        cursor.execute('UPDATE Book SET name = TRIM(%s), description = TRIM(%s) WHERE id = %s ',(name,description,id))
    except:
        print("Неверные значения")
    connectBD.conn.commit()
    cursor.close()

def UpdateBookDepository(id, name, place):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('UPDATE Book_Depository SET name = (%s), place = (%s) WHERE id = %s ',(name,place,id,))
    connectBD.conn.commit()
    cursor.close()


def UpdateBookAuthor(book,author ):
    #   20.09.2024
    #вставка новой связи между автором и книгой - не сделано? 
    cursor = connectBD.conn.cursor()
    cursor.execute('UPDATE Book_Author SET author_id = (%s) WHERE book_id = %s',(author,book))
    connectBD.conn.commit()
    cursor.close()