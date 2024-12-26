from Base.connect import conn

def ExistForId(id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tanks WHERE id = %s',(id,))
    result = cursor.fetchall()
    cursor.close()
    return (result != [])

def IfList(id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tanks WHERE parent_id = %s',(id,))
    result = cursor.fetchall()
    cursor.close()
    return (result == [])

def GetMax():
    cursor = conn.cursor()
    cursor.execute('SELECT max(id) FROM tanks')
    result = cursor.fetchall()
    cursor.close()
    return (result)