import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
from Base import UPDATEs
import os
import time

def Redact():
    id = int(input("Введите id книги для редактирования "))
    name = input("Введите новое ФИО ")
    UPDATEs.UpdateAuthor(id,name)

def Delete():
    id = int(input("Введите id удаляемого автора"))
    DELETEs.DeleteAuthor(str(id))

def Insert():
    name = input("Введите ФИО ")
    INSERTs.InsertAuthor(name)

def PrintAll():
    arr = SELECTs.GetAllAuthor()
    for i in arr:
        print(i)
    time.sleep(5)

def Print():
    id = int(input("Введите id "))
    arr = SELECTs.GetAuthor(id)
    print(arr)
    time.sleep(5)
