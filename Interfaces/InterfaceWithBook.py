import CRUD
from CRUD import CRUD_for_book
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
        CRUD_for_book.InsertBook()
    if(x==2):
        CRUD_for_book.DeleteBook()
    if(x==3):
        CRUD_for_book.RedactBook()
    if(x==4):
        CRUD_for_book.PrintAllBook()
