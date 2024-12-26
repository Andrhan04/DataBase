from Base import Procedures

#  Табличный вывод


# Получение номера действия
def get_action_number():
    print("""
            0 - Выход
            1 - Добавить книгохранилище
            2 - Получить все книгохранилища
            3 - Получить книгохранилище по id
            4 - Редактирование книгохранилище
            5 - Удалить одно книгохранилище по id
            6 - Удалить несколько пользователей            
        """)
    while(True):
        try:
            choosing_of_action = int(input("Введите номер действия: ")) 
            return choosing_of_action    
        except:
            print("Вы ввели не число. Повторите ввод.")


from Base.connectBD import conn
import os
os.system('cls')
while(True):
    number_of_acion = get_action_number()
    if(number_of_acion == 0): # Выход
        os.system('cls')
        conn.close()
        break

    elif(number_of_acion == 1): # Добавить пользователя
        Procedures.Add(conn)

    elif(number_of_acion == 2): # Получить всех пользователей
        Procedures.GetAll(conn)
     
    elif(number_of_acion == 3): # Получить определенного пользователя по ключу
        Procedures.Get(conn=conn)
        
    elif(number_of_acion == 4): # Редактирование пользователя
        Procedures.Update(conn)
            
    elif(number_of_acion == 5): # Удалить пользователя
        Procedures.Delete(conn)

    elif(number_of_acion == 6): # Удалить несколько пользователей
        Procedures.DeleteMany(conn)


   
        
