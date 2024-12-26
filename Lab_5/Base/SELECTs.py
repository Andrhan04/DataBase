import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os


def GetAll():
    #Вывод в консоль всех Авторов
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Author ')
    result =cursor.fetchall()
    cursor.close()
    return sorted(result)

def Get(id):
    cursor = connectBD.conn.cursor()
    cursor.execute('SELECT * FROM Author WHERE id = %s',(id,))
    result = cursor.fetchall()
    #print(cursor.fetchall())
    cursor.close()
    return sorted(result)


def GetForAtribute(name, limit, offset):
    cursor = connectBD.conn.cursor()
    cursor.execute("SELECT * FROM Author WHERE ' '||LOWER(name)||' ' ILIKE %s LIMIT %s OFFSET %s",('%'+name+'%',limit,offset))
    result = cursor.fetchall()
    cursor.close()
    return sorted(result)