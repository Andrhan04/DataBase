import os
from Base import connectBD
def Work():
    print("Для закрытия нажми 0")
    print("Для работы с книгой нажми 1")
    print("Для работы с автором нажми 2")
    print("Для работы с книгохранилищем нажми 3")


x = 1
while(True):
    os.system('cls')
    Work()
    x =int(input())        
    if(x==1):
        import Interfaces.InterfaceWithBook as inter
        inter.main()
        #print(1)
    elif(x==2):
        import Interfaces.InterfaceWithAuthor as interA
        interA.main()
        #print(2)
    elif(x==3):
        import Interfaces.InterfaceWithPlace as interP
        interP.main()
        #print(3)
    else:
        break



os.system('cls')
os.system('exit')
connectBD.conn.close()
#ЛБ №2. Поиск и пагинация
# Реализовать функцию поиска экземпляров сущности по указанным пользователем значениям атрибутов.
# Метод Model_nameSearch() принимает
#       список значений атрибутов поиска модели и 
#       параметры количества выдаваемых результатов (по умолчанию = 5) и 
#       смещения (по умолчанию = 0).
# Дополнительная задача 1.
# - код закоммичен в репозиторий git из ЛБ №0
