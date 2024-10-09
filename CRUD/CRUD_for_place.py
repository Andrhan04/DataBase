import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
from Base import UPDATEs
import os
import time

def Redact():
    id = int(input("Введите id для редактирования "))
    name = input("Введите новое название ")
    place = input("Введите новое место ")
    UPDATEs.UpdateBookDepository(id,name,place)

def Delete():
    id = int(input("Введите id удаляемого автора"))
    DELETEs.DeleteBookDepo(str(id))

def Insert():
    name = input("Введите ФИО ")
    place = input("Введите новое место ")
    INSERTs.InsertBook_Depository(name,place)

def PrintAll():
    arr = SELECTs.GetAllPlace()
    for i in arr:
        print(i)
    time.sleep(5)

def Print():
    id = int(input("Введите id "))
    arr = SELECTs.GetPlace(id)
    print(arr)
    time.sleep(5)
