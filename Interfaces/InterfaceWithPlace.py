import CRUD
from CRUD import CRUD_for_place as CRUD
import os

def Mydef():
    os.system('cls')
    print("Для вставки новой записи нажмите 1")
    print("Для удаления нажмите 2")
    print("Для редактировани нажмите 3")
    print("Для получения всех нажмите 4")
    print("Для получения нажмите 5")
    print("Для выхода нажмите 0")


x = 1
while(x != 0):
    Mydef()
    x = int(input())
    os.system('cls')
    if(x==1):
        CRUD.Insert()
    if(x==2):
        CRUD.Delete()
    if(x==3):
        CRUD.Redact()
    if(x==4):
        CRUD.PrintAll()
    if(x==5):
        CRUD.Print()
