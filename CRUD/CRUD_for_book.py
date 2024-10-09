import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
from Base import UPDATEs
import os
import time

def Redact():
    id = 1
    while(True):
        try:
            id = int(input("Введите id книги для редактирования "))
            old_name = SELECTs.GetBook(id)
            old_name[0][0]
            break
        except:
            print("Что то не то")
            time.sleep(2)

    print("Старые занчения")
    print(old_name[0])
    name = input("Введите новое название книги ")
    if(name == ""): name = old_name[0][1]
    description = input("Введите новое описание ")
    if(description == ""): description = old_name[0][2]
    UPDATEs.UpdateBook(id,name,description)

def Delete():
    try:
        id = int(input("Введите id удаляемой книги "))
        DELETEs.DeleteBook(str(id))
    except:
        print("Что то не то")
        time.sleep(2)
        return


def Insert():
    name = input("Введите название книги ")
    description = input("Введите описание ")
    INSERTs.InsertBook(name,description)

def PrintAll():
    arr = SELECTs.GetAllBook()
    for i in arr:
        print(i)
    i = input()

def Print():
    id = 1
    while(True):
        try:
            id = int(input("Введите id книги "))
            arr = SELECTs.GetBook(id)
            arr[0][0]
            break
        except:
            print("Что то не то")
            time.sleep(2)
    print(arr)
    i = input()

def DeleteMany():
    list_of_id = []
    for element in input("Введите идентификационный номер: ").split():
        if(element.isdigit()):
            list_of_id.append(((element),))
        else:
            print("Не число")
    DELETEs.DeleteBookMany(list_of_id)