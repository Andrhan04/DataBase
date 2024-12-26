from Base import query
import os
import time

# Получение номера действия
def get_action_number():
    print("""
            0 - Выход
            1 - Добавить лист
            2 - Удалить лист
            3 - Удалить поддерево  
            4 - Удалить узел без поддерева
            5 - Получить прямых потомков
            6 - Получить прямого родителя
            7 - Получить всех потомков
            8 - Получить всех родителей     
            9 - Получить всё дерево 
        """)
    while(True):
        try:
            choosing_of_action = int(input("Введите номер действия: ")) 
            return choosing_of_action    
        except:
            print("Вы ввели не число. Повторите ввод.")


from Base import connect as Connect
conn = Connect.conn

while(True):
    number_of_acion = get_action_number()
    if(number_of_acion == 0): # Выход
        conn.close()
        os.system('cls')
        break

    elif(number_of_acion == 1): # Добавить лист
        print(query.AddLeaf(conn))
        os.system('cls')

    elif(number_of_acion == 2): # Удалить лист
        print(query.DeleteLeaf(conn))
        os.system('cls')

    elif(number_of_acion == 3): # Удалить поддерево          
        print(query.DeleteSubtree(conn))
        os.system('cls')       

    elif(number_of_acion == 4): # Удалить узел без поддерева 
        print(query.DeleteNode(conn))
        os.system('cls')
        
    elif(number_of_acion == 5): # Получить прямых потомков
        result = query.GetDirectDescendants(conn)
        
        query.PrintBeautifully(result)
        
    elif(number_of_acion == 6): # Получить прямого родителя
        result = query.GetDirectParent(conn)
        query.PrintBeautifully(result)        

    elif(number_of_acion == 7): # Получить всех потомков
        result = query.GetAllDescendants(conn=conn)
        query.PrintBeautifully(result)
    
    elif(number_of_acion == 8): # Получить всех родителей
        result = query.GetAllParents(conn)
        query.PrintBeautifully(result)
        
    elif(number_of_acion == 9): # Получить все дерево
        os.system('cls')
        result = query.GetAll(conn=conn)
        query.PrintBeautifully(result)
