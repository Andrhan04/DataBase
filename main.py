import os
def Work():
    print("Для закрытия нажми 0")
    print("Для работы с книгой нажми 1")
    print("Для работы с автором нажми 2")
    print("Для работы с книго хранилищем нажми 3")


x = 1
while(x != 0):
    os.system('cls')
    Work()
    x =int(input())        
    if(x==1):
        import Interfaces.InterfaceWithBook
    if(x==2):
        import Interfaces.InterfaceWithAuthor
    if(x==3):
        #import Interfaces.InterfaceWithPlace
        print(3)



 
os.system('cls')
os.system('exit')


