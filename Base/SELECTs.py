import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os

def GetAllBook():
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

def GetBook(id):
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Book WHERE id = %s',(id,))
    result = cursor.fetchall()
    #print(cursor.fetchall())
    cursor.close()
    return sorted(result)

def GetPlace(id):
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Book_Depository WHERE id = %s',(id,))
    result = cursor.fetchall()
    #print(cursor.fetchall())
    cursor.close()
    return sorted(result)

def GetAuthor(id):
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Author WHERE id = %s',(id,))
    result = cursor.fetchall()
    #print(cursor.fetchall())
    cursor.close()
    return sorted(result)


def GetBookForName(name, limit, offset):
    cursor = connectBD.conn.cursor()
    cursor.execute("SELECT * FROM Book WHERE ' '||LOWER(name)||' ' ILIKE %s LIMIT %s OFFSET %s",('%'+name+'%',limit,offset))
    result = cursor.fetchall()
    cursor.close()
    return sorted(result)

def GEtBookForDesc(description, limit, offset):
    cursor = connectBD.conn.cursor()
    if(description == ""):
        cursor.execute("SELECT * FROM Book WHERE LOWER(description) ILIKE %s LIMIT %s OFFSET %s",(description,limit,offset))
    else:
        cursor.execute("SELECT * FROM Book WHERE LOWER(description) ILIKE %s LIMIT %s OFFSET %s",('%'+description+'%',limit,offset))
    result = cursor.fetchall()
    cursor.close()
    return sorted(result)

def GetBookForAtribute(name, description, limit, offset):
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Book WHERE ' '||LOWER(name)||' ' ILIKE %s AND LOWER(description) ILIKE %s LIMIT %s OFFSET %s',('%'+name+'%','%'+description+'%',limit,offset))
    result = cursor.fetchall()
    cursor.close()
    return sorted(result)