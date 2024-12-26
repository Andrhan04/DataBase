import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD
import os

def Delete(id,):
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM Author WHERE id = %s',(id,))
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res

def DeleteMany(list_of_id,):
    cursor = connectBD.conn.cursor()
    s = ""
    for lst in list_of_id:
        for id in lst:
            Delete(id)
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res























#   Удаление всех книг соавторов автора <> в которых не было автора <>
#   Потом попробую
