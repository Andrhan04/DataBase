import os
def Work():
    print("Для закрытия нажми 0")
    print("Для работы с книгой нажми 1")
    print("Для работы с автором нажми 2")
    print("Для работы с книгохранилищем нажми 3")


x = 1
while(x != 0):
    os.system('cls')
    Work()
    x =int(input())        
    if(x==1):
        import Interfaces.InterfaceWithBook as inter
        inter.main()
        #print(1)
    elif(x==2):
        import Interfaces.InterfaceWithAuthor as interA
        #interA.main()
        #print(2)
    elif(x==3):
        import Interfaces.InterfaceWithPlace as inter
        #inter.main()
        #print(3)
    else:
        break


os.system('cls')
os.system('exit')