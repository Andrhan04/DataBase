import os
def Work():
    print("Для закрытия нажми 0")
    print("Для работы с книгой нажми 1")

x = 1
while(x != 0):
    os.system('cls')
    Work()
    x =int(input())        
    if(x==1):
        import Interfaces.InterfaceWithBook as InterfaceWithBook


 
os.system('cls')
os.system('exit')


