import hashlib

def Add(conn):
    name = input("Введите название: ")    
    place = input("Введите место расположение: ")
    try:
        cursor = conn.cursor()
        cursor.execute("CALL add(%s, %s)", (name, place))
        conn.commit()
        print("Книгохранилище успешно добавлено.")
    except Exception as e:
        conn.rollback()
        print(e)

def GetAll(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM get_all()")
    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[0]:3} {row[1]:35} {row[2]}")


def Get(conn):
    id = input("Введите ID : ")    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM get(%s)", (id,))
        result = cursor.fetchone()
        if result:
            print("{:<20} {}".format("id:", result[0]))
            print("{:<20} {}".format("Название:", result[1]))
            print("{:<20} {}".format("Место:", result[2]))
        else:
            print(f"Book depository with ID {id} not found.")
    except Exception as e:
        conn.rollback()
        print(e)

def Update(conn):
    id = input("Введите ID: ")    
    name = input("Введите название: ")
    place = input("Введите место: ")
    
        
    try:
        cursor = conn.cursor()
        cursor.execute("CALL update(%s, %s, %s)",
                        (id, name, place))
        conn.commit()
        print("Книгохранилище успешно обновлено.")
    except Exception as e:
        conn.rollback()
        print(e)

def Delete(conn):
    id = input("Введите ID: ")
    try:
        cursor = conn.cursor()
        cursor.execute("CALL delete(%s)", (id,))
        conn.commit()
        print("Книгохранилище успешно удалено.")
    except Exception as e:
        conn.rollback()
        print(f"Произошла ошибка: {e}")

def DeleteMany(conn):
    ids_input = input("Введите id книгохранилищ через пробел: ")    

    ids = ids_input.split()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT delete_many(%s)", (ids,))
        deleted_count = cursor.fetchone()[0]
        conn.commit()
        print(f"Удалено книгохранилищ: {deleted_count}")
    except Exception as e:
        conn.rollback()
        print(e)