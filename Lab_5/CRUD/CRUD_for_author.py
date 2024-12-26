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
            id = int(input("Введите id для редактирования "))
            old_name = SELECTs.Get(id)
            old_name[0][0]
            break
        except:
            print("Что то не то с id")
    print("Старые занчения")
    print(old_name[0])
    name = input("Введите новое ФИО (Если не хочешь изменять нажми enter) ")
    if(name == ""): name = old_name[0][1]
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
