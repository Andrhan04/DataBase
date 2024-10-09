import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os

def DeleteBook(id,):
    # 19.09.2024 удаление книги по id и связей с ней
    # возвращает колличество строк попавших в запрос
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM Book WHERE id = %s',(id,))
    cursor.execute('DELETE FROM Book_Author WHERE book_id = %s', (id,))
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res

def DeleteBookMany(list_of_id,):
    # 19.09.2024 удаление книги по id и связей с ней
    # возвращает колличество строк попавших в запрос
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM Book WHERE id = %s',(list_of_id,))
    cursor.execute('DELETE FROM Book_Author WHERE book_id = %s', (list_of_id,))
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res

def DeleteAuthor(id):
    # 20.09.2024 удаление автора по id и связей с ним
    # возвращает колличество строк попавших в запрос
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM Author WHERE id = %s', (str(id), ))
    cursor.execute('DELETE FROM Book_Author WHERE author_id = %s', id)
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res


def DeleteBookAuthor(book_id, author_id):
    #20.09.2024 удаление связи автора и книги
    # возвращает колличество строк попавших в запрос
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM Book_Author WHERE author_id = %s AND book_id = %s', book_id, author_id)
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res
    
def DeleteBookDepository(id):
    #20.09.2024 удаление связи автора и книги
    # возвращает колличество строк попавших в запрос
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM Book_Depository WHERE id = %s', (id,))
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res






















#   Удаление всех книг соавторов автора <> в которых не было автора <>
#   Потом попробую
