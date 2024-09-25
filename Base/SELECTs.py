import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os

def GetAllBook():
    #Вывод в консоль все книги
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Book ')
    result = cursor.fetchall()
    #print(cursor.fetchall())
    cursor.close()
    return sorted(result)

def GetAllAuthor():
    #Вывод в консоль всех Авторов
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Author ')
    result =cursor.fetchall()
    cursor.close()
    return sorted(result)

def GetAllPlace():
    #Вывод в консоль всех Книгохранилищ
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Book_Depository ')
    result = cursor.fetchall()
    cursor.close()
    return sorted(result)

def GetAllBoohAuthor():
    #Вывод в консоль всех Книгохранилищ
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Book_Author ')
    result = cursor.fetchall()
    cursor.close()
    return sorted(result)