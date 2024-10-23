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
            print("Что то не то с id")
    print("Старые занчения")
    print(old_name[0])
    name = input("Введите новое название книги (Если не хочешь изменять нажми enter) ")
    if(name == ""): name = old_name[0][1]
    description = input("Введите новое описание (Если не хочешь изменять нажми enter) ")
    if(description == ""): description = old_name[0][2]
    print(UPDATEs.UpdateBook(id,name,description))

def Delete():
    PrintAll()
    try:
        id = int(input("Введите id удаляемой книги "))
        i = DELETEs.DeleteBook(str(id))
        return i
    except:
        print("Что то не то с id")
        return 0


def Insert():
    name = input("Введите название книги ")
    description = input("Введите описание ")
    print(INSERTs.InsertBook(name,description))

def PrintAll():
    arr = SELECTs.GetAllBook()
    for element in arr:
        print("{:3d}     {:30s} {:s}".format(element[0],element[1],element[2]))
    print("Для закрытия введи что-нибудь")
    

def Print():
    id = 1
    while(True):
        try:
            id = int(input("Введите id книги "))
            arr = SELECTs.GetBook(id)
            arr[0][0]
            break
        except:
            print("Что то не то с id")
            time.sleep(2)
    for element in arr:
        print("{:3d}     {:30s} {:s}".format(element[0],element[1],element[2]))
    print("Для закрытия введи что-нибудь")

def DeleteMany():
    PrintAll()
    list_of_id = []
    for element in input("Введите идентификационные номера через пробел: ").split():
        if(element.isdigit()):
            list_of_id.append(((element),))
        else:
            print("Что то не то с id")
    DELETEs.DeleteBookMany(list_of_id)