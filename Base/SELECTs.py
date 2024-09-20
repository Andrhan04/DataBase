import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD

def GetAllBook():
    #Вывод в консоль все книги
    cursor = connectBD.conn.cursor()
    result = cursor.execute('SELECT * FROM Book ')
    print(cursor.fetchall())
    cursor.close()

def GetAllAuthor():
    #Вывод в консоль всех Авторов
    cursor = connectBD.conn.cursor()
    result = cursor.execute('SELECT * FROM Author ')
    print(cursor.fetchall())
    cursor.close()
    return result

def GetAllPlace():
    #Вывод в консоль всех Книгохранилищ
    cursor = connectBD.conn.cursor()
    result = cursor.execute('SELECT * FROM Book_Depository ')
    print(cursor.fetchall())
    cursor.close()
    return result
