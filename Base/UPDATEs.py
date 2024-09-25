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

def UpdateBook(id, name, description, place):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('UPDATE Book SET name = (%s), description = (%s), place_id = (%s) WHERE id = %s ',(name,description,place,id,))
    connectBD.conn.commit()
    cursor.close()

def UpdateBookDepository(id, name, place):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('UPDATE Book_Depository SET name = (%s), place = (%s) WHERE id = %s ',(name,place,id,))
    connectBD.conn.commit()
    cursor.close()

def UpdateBookAuthor(old_book_id, old_author_id, new_book_id, new_author_id):
    #   19.09.2024
    #Вставка нового автора
    cursor = connectBD.conn.cursor()
    cursor.execute('UPDATE Book_Author SET book_id = (%s), author_id = (%s) WHERE book_id = %s AND author_id = %s',(new_book_id, new_author_id, old_book_id, old_author_id, ))
    connectBD.conn.commit()
    cursor.close()
