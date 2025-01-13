from Classes.Book_depository import Book_depository
from Classes.connect import conn
import os
# Получение номера действия
def get_action_number():
    print("""
            0 - Выход
            1 - Добавить
            2 - Получить все
            3 - Получить по id
            4 - Редактирование
            5 - Удалить по id
            6 - Удалить несколько            
        """)
    while(True):
        try:
            choosing_of_action = int(input("Введите номер действия: ")) 
            return choosing_of_action
        except:
            print("Вы ввели не число. Повторите ввод.")

def main():
    book = Book_depository()
    while(True):
        chose = get_action_number()
        if(chose == 0):
            os.system('cls')
            conn.close()
            return 
        elif(chose == 1): # Добавить
            book.add()

        elif(chose == 2): # Получить всех 
            os.system('cls')
            result = book.getAll()
            if(len(result) != 0):
                for element in result:
                    print("{:3d}     {:30s} {:s}".format(element[0],element[1],element[2]))
        
        elif(chose == 3): # Получить по ключу
            while(True):
                try:
                    id = int(input("Введите id (целое положительное число ): ")) 
                    if id > 0:
                        break
                    else:
                        print("Вы ввели не положительное число. Повторите ввод.")
                except:
                    print("Вы ввели не целое число. Повторите ввод.")
            result = book.get(id)
            if(len(result) != 0):
                for element in result:
                    print("{:3d}     {:30s} {:s}".format(element[0],element[1],element[2]))

        elif(chose == 4): # Редактирование 
            while(True):
                try:
                    id = int(input("Введите id (целое положительное число ): ")) 
                    if id > 0:
                        break
                    else:
                        print("Вы ввели не положительное число. Повторите ввод.")
                except:
                    print("Вы ввели не целое число. Повторите ввод.")
            book.update(id)
                
        elif(chose == 5): # Удалить 
            while(True):
                try:
                    id = int(input("Введите id (целое положительное число ): ")) 
                    if id > 0:
                        break
                    else:
                        print("Вы ввели не положительное число. Повторите ввод.")
                except:
                    print("Вы ввели не целое число. Повторите ввод.")
            book.delete(id)

        elif(chose == 6): # Удалить несколько 
            arr = input("Введите id через пробел: ").split()
            book.deleteMany(arr)

main()