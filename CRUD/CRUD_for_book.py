import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
from Base import UPDATEs
import os
import time

def Redact():
    id = int(input("Введите id книги для редактирования "))
    name = input("Введите новое название книги ")
    description = input("Введите новое описание ")
    UPDATEs.UpdateBook(id,name,description)

def Delete():
    id = int(input("Введите id удаляемой книги "))
    DELETEs.DeleteBook(str(id))

def Insert():
    name = input("Введите название книги ")
    description = input("Введите описание ")
    INSERTs.InsertBook(name,description)

def PrintAll():
    arr = SELECTs.GetAllBook()
    for i in arr:
        print(i)
    time.sleep(5)

def Print():
    id = int(input("Введите id книги "))
    arr = SELECTs.GetBook(id)
    print(arr)
    time.sleep(5)
