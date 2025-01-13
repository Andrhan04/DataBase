import psycopg2
conn = psycopg2.connect(dbname = "Base",
                        user="postgres",
                        password="pass",
                        host="127.0.0.1",
                        port="5432")

class Book_depository:
    def __init__(self):
        self.conn = conn
        self.cursor = self.conn.cursor()
    def add(self):
        name = input("Введите название книги ").strip()
        place = input("Введите описание ").strip()
        while name.find('  ') != -1:
            name = name.replace('  ', ' ')
        while place.find('  ') != -1:
            place = place.replace('  ', ' ')
        if(name == ""):
            print("Название не может быть пустым")
            return
        if(place == ""):
            print("Описание не может быть пустым")
            return
        cursor = conn.cursor()
        cursor.execute('INSERT INTO book_depository (name,place) VALUES (TRIM(%s),TRIM(%s))',(name,place))
        conn.commit()

    def deleteMany(self,list_id):
        for id in list_id:
            if(id.isdigit() == True):
                self.delete(id)

    def delete(self,id):
        data = self.get(id)
        if(len(data) == 0):
            return
        self.cursor.execute('DELETE FROM book_depository WHERE id = %s',(id,))
        res = self.cursor.rowcount
        self.conn.commit()
        return res

    def update(self, id):
        name = input("Введите название книги ")
        place = input("Введите описание ")
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE book_depository SET name = TRIM(%s), place = TRIM(%s) WHERE id = %s ',(name,place,str(id)))
        except:
            print("Неверные значения")
        conn.commit()
        cursor.close()

    def get(self, my_id):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM book_depository WHERE id = %s AND del = false',(my_id,))
        result = cursor.fetchall()
        return result

    def getAll(self):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM book_depository WHERE del = false')
        result = cursor.fetchall()
        #print(result)
        cursor.close()
        arr = sorted(result)
        # for element in arr:
        #     print("{:3d}     {:30s} {:s}".format(element[0],element[1],element[2]))
        return arr