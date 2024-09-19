import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import Base
from Base import connectBD

def DeleteBook(id):
    # 19.09.2024 удаление книги по id
    # возвращает колличество строк попавших в запрос
    cursor = connectBD.conn.cursor()
    cursor.execute('DELETE FROM "Book" WHERE id = %s', id)
    res = cursor.rowcount
    connectBD.conn.commit()
    cursor.close()
    return res