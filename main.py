import Base
from Base import SELECTs
from Base import INSERTs
from Base import DELETEs
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

#INSERTs.InsertBook_Depository("Научная Библиотека","Ербанова д.79")
#INSERTs.InsertBook("Учебник","Русский язык 6 класс", "1")
#INSERTs.InsertBook("Учебник","Математика язык 6 класс", "5")
#INSERTs.InsertBook("Отцы и дети","Тут нет никакого описания", "7")
#INSERTs.InsertBook("Ася","Я не смог придумать", "8")
#INSERTs.InsertBook("Евгений Онегин","Роман", "9")
#INSERTs.InsertBook("Сказка о рыбаке и рыбаке","Сказка о рыбаке и рыбке рассказывает нам о старике, в сети которого однажды попалась золотая рыбка.", "9")
#INSERTs.InsertBook("Капитанская дочка","Действие происходит во время восстания Емельяна Пугачёва.", "4")
#INSERTs.InsertBook("Герой нашего времени","1837 год: еще один год изнурительной кавказской войны. Молодой офицер Григорий Печорин за участие в дуэли отправлен в ссылку в действующую...", "3")
#INSERTs.InsertBook("Мертвые души","Это произведение не о том что ты думаешь", "10")
#INSERTs.InsertBook("Миргород","Сборник", "2")
#INSERTs.InsertBook("Идиот","Я не читал, а искать лень", "6")

#INSERTs.InsertBook_Depository("Центральная Библиотека","Ленина д.15")
#INSERTs.InsertBook_Depository("Библиотека имени Гайдара","Пушкина д.24")
#INSERTs.InsertBook_Depository("Библиотека имени Пушкина","Ербанова д.15")
#INSERTs.InsertBook_Depository("Национальная Библиотека","проспект Победы д.17")
#INSERTs.InsertBook_Depository("Национальная Библиотека","проспект Победы д.8")
#INSERTs.InsertBook_Depository("Республиканская Библиотека","бульвар Карла-Маркса д.18")
#INSERTs.InsertBook_Depository("Детская Библиотека","Ключевская д.13")
#INSERTs.InsertBook_Depository("Юнешская Библиотека","Геологическая д.23")
#INSERTs.InsertBook_Depository("Библиотека имени Калашникова","проспект Строитнелей д.27")

#INSERTs.InsertBookAuthor("1","2")
#INSERTs.InsertBookAuthor("2","3")
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