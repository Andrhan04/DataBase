import CRUD
from CRUD import CRUD_for_book as CRUD
import os

def Mydef():
    os.system('cls')
    print("Для вставки новой книги нажмите 1")
    print("Для удаления книги нажмите 2")
    print("Для редактирования книги нажмите 3")
    print("Для получения всех книги нажмите 4")
    print("Для получения книги нажмите 5")
    print("Для удаления книг нажмите 6")
    print("Для выхода нажмите 0")

def main():
    while(True):
        Mydef()
        x = int(input())
        os.system('cls')
        if(x==1):
            CRUD.Insert()
        elif(x==2):
            CRUD.Delete()
        elif(x==3):
            CRUD.Redact()
        elif(x==4):
            CRUD.PrintAll()
        elif(x==5):
            CRUD.Print()
        elif(x==6):
            CRUD.DeleteMany()
        else:
            break
    return 0
