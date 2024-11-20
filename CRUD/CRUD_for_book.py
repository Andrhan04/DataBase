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


def Find():
    try:
        x = int(input("Для поиска по названию нажми 1, по описанию 2, по описанию и названию 3\n"))
    except:
        input("x не число (Для закрытия введи что-нибудь)")
        return
    limit = 1
    try:
        limit = int(input("Введите максимальное колличество книг для получения (Если стандартное то введи q)"))
    except:
        limit = 5
    if(limit < 0 or limit >= 32768):
        limit = 5
    
    offset = 0
    try:
        offset = int(input("Введите смещение (Если стандартное то введи q)"))
    except:
        offset = 0
    
    if(offset < 0 or offset >= 32768):
        offset = 0
    if(x == 1):
        name = input("Введите название книги ")
        if(name == ""):
            print("Нет ничего с пустым названием")
            return
        else:
            while(name.find('  ') >= 0):
                name = name.replace('  ', ' ')
            arr = SELECTs.GetBookForName(name,limit,offset)
    elif(x==2):
        description = input("Введите описание ")
        while(description.find('  ')>=0):
                description= description.replace('  ', ' ')
        arr = SELECTs.GEtBookForDesc(description,limit,offset)
    elif(x==3):
        name = input("Введите название книги ")
        description = input("Введите описание ")
        if(name == ""):
            print("Нет ничего с пустым названием")
            return
        else:
            while(name.find('  ') >= 0):
                name = name.replace('  ', ' ')
            while(description.find('  ')>=0):
                description= description.replace('  ', ' ')
            arr = SELECTs.GetBookForAtribute(name,description,limit,offset)
    else:
        print("Нет такой функции")

    if(arr == []):
        print("НЕТУ НИЧЕГО")
    else:
        for element in arr:
            print("{:3d}     {:30s} {:s}".format(element[0],element[1],element[2]))
    input("Для закрытия введи что-нибудь")
    return
    