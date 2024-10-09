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
    elif(x==2):
        import Interfaces.InterfaceWithAuthor
    elif(x==3):
        import Interfaces.InterfaceWithPlace
        #print(3)
    else:
        break



 
os.system('cls')
os.system('exit')


