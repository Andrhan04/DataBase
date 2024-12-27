import hashlib

def Add(conn):
    name = input("Введите название: ")    
    try:
        cursor = conn.cursor()
        print(name)
        #cursor.execute("CALL add('%s')", str(name))
        s = "CALL add('" + name + "')"
        cursor.execute(s)
        conn.commit()
        print("Автор успешно добавлено.")
    except Exception as e:
        conn.rollback()
        print(e)

def GetAll(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM get_all()")
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[0]:3} {row[1]:35}")


def Get(conn):
    id = input("Введите ID : ")    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM get(%s)", (id,))
        result = cursor.fetchone()
        if result:
            print("{:<20} {}".format("id:", result[0]))
            print("{:<20} {}".format("Название:", result[1]))
        else:
            print(f"Author with ID {id} not found.")
    except Exception as e:
        conn.rollback()
        print(e)

def Update(conn):
    id = input("Введите ID: ")    
    name = input("Введите название: ")
    
        
    try:
        cursor = conn.cursor()
        cursor.execute("CALL update(%s, %s)",
                        (id, name))
        conn.commit()
        print("Автор успешно обновлено.")
    except Exception as e:
        conn.rollback()
        print(e)

def Delete(conn):
    id = input("Введите ID: ")
    try:
        cursor = conn.cursor()
        cursor.execute("CALL delete(%s)", (id,))
        conn.commit()
        print("Автор успешно удалено.")
    except Exception as e:
        conn.rollback()
        print(f"Произошла ошибка: {e}")

def DeleteMany(conn):
    ids_input = input("Введите id авторов через пробел: ")    

    ids = ids_input.split()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT delete_many(%s)", (ids,))
        deleted_count = cursor.fetchone()[0]
        conn.commit()
        print(f"Удалено авторов: {deleted_count}")
    except Exception as e:
        conn.rollback()
        print(e)