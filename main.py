import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
from Base import UPDATEs
import CRUD
import os

def Mydef():
    os.system('cls')
    print("Для вставки новой книги нажмите 1")
    print("Для удаления книги нажмите 2")
    print("Для редактирования книги нажмите 3")
    print("Для получения всех книги нажмите 4")
    print("Для выхода нажмите 0")


x = 1
while(x != 0):
    Mydef()
    x = int(input())
    os.system('cls')
    if(x==1):
        CRUD.InsertBook()
    if(x==2):
        CRUD.DeleteBook()
    if(x==3):
        CRUD.RedactBook()
    if(x==4):
        CRUD.PrintAllBook()
