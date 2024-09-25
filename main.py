import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
from Base import UPDATEs
import os

#INSERTs.InsertAuthor("Львов_Валентин_Витальевич")
#INSERTs.InsertAuthor("Наум_Яковлевич_Виленкин")
#INSERTs.InsertAuthor("Владимир_Иванович_Жохов")
#INSERTs.InsertAuthor("Чесноков_Александр_Семёнович")
#INSERTs.InsertAuthor("Львова_Светлана_Ивановна")
#INSERTs.InsertAuthor("Иваан_Сергееевич_Тургенев")
#INSERTs.InsertAuthor("Пушкин_Александр_Сереевич")
#INSERTs.InsertAuthor("Лермонтов_Михаил_Юрьевич")
#INSERTs.InsertAuthor("Гоголь_Николай_Васильевич")
#INSERTs.InsertAuthor("Достоевский_Фёдор_Михайлович")

#INSERTs.Create()
#INSERTs.InsertBook("Учебник","Математика язык 6 класс")
#INSERTs.InsertBook("Отцы и дети","Тут нет никакого описания")
#INSERTs.InsertBook("Ася","Я не смог придумать")
#INSERTs.InsertBook("Евгений Онегин","Роман")
#INSERTs.InsertBook("Учебник","Русский язык 6 класс")
#INSERTs.InsertBook("Сказка о рыбаке и рыбаке","Сказка")
#INSERTs.InsertBook("Капитанская дочка","Действие происходит во время восстания Емельяна Пугачёва.")
#INSERTs.InsertBook("Герой нашего времени","1837 год: еще один год изнурительной кавказской войны...")
#INSERTs.InsertBook("Мертвые души","Это произведение не о том что ты думаешь")
#INSERTs.InsertBook("Миргород","Сборник")
#INSERTs.InsertBook("Идиот","Я не читал, а искать лень")


#INSERTs.InsertBook_Depository("Научная Библиотека","Ербанова д.79")
#INSERTs.InsertBook_Depository("Центральная Библиотека","Ленина д.15")
#INSERTs.InsertBook_Depository("Библиотека имени Гайдара","Пушкина д.24")
#INSERTs.InsertBook_Depository("Библиотека имени Пушкина","Ербанова д.15")
#INSERTs.InsertBook_Depository("Национальная Библиотека","проспект Победы д.17")
#INSERTs.InsertBook_Depository("Национальная Библиотека","проспект Победы д.8")
#INSERTs.InsertBook_Depository("Республиканская Библиотека","бульвар Карла-Маркса д.18")
#INSERTs.InsertBook_Depository("Детская Библиотека","Ключевская д.13")
#INSERTs.InsertBook_Depository("Юнешская Библиотека","Геологическая д.23")
#INSERTs.InsertBook_Depository("Библиотека имени Калашникова","проспект Строитнелей д.27")

#INSERTs.InsertBookAuthor("2","3")
#INSERTs.InsertBookAuthor("1","2")
#INSERTs.InsertBookAuthor("1","1")
#INSERTs.InsertBookAuthor("2","4")
#INSERTs.InsertBookAuthor("2","5") 
#INSERTs.InsertBookAuthor("3","6")
#INSERTs.InsertBookAuthor("4","6")
#INSERTs.InsertBookAuthor("5","7")
#INSERTs.InsertBookAuthor("6","7")
#INSERTs.InsertBookAuthor("7","7")
#INSERTs.InsertBookAuthor("8","8")
#INSERTs.InsertBookAuthor("9","9")
#INSERTs.InsertBookAuthor("10","9")
#INSERTs.InsertBookAuthor("11","10")

#UPDATEs.UpdateBookAuthor("1","0","1", "1")

#INSERTs.InsertInstance('1',"1")
INSERTs.InsertInstance('11',"6")
INSERTs.InsertInstance('2',"5")
INSERTs.InsertInstance('3',"7")
INSERTs.InsertInstance('4',"8")
INSERTs.InsertInstance('5',"9")
INSERTs.InsertInstance('6',"9")
INSERTs.InsertInstance('7',"4")
INSERTs.InsertInstance('8',"3")
INSERTs.InsertInstance('9',"10")
INSERTs.InsertInstance('10',"2")


arr = SELECTs.GetAllAuthor()
print("-------------------------------")
for i in arr:
    print(i)
arr = SELECTs.GetAllBook()
print("-------------------------------")
for i in arr:
    print(i)
arr = SELECTs.GetAllPlace()
print("-------------------------------")
for i in arr:
    print(i)

arr = SELECTs.GetAllBoohAuthor()
print("-------------------------------")
for i in arr:
    print(i)