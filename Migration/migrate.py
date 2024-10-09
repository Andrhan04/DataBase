import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="pass",
    host="127.0.0.1",
    port="5432"
)
cursor = conn.cursor()

cursor.execute('''
   CREATE TABLE Book (id SERIAL PRIMARY KEY, name TEXT, Description TEXT);
               ''')
cursor.execute('''
    CREATE TABLE author (id SERIAL PRIMARY KEY, fio TEXT);
               ''')
cursor.execute('''
    CREATE TABLE book_depository (id SERIAL PRIMARY KEY, name TEXT, place TEXT);
               ''')
cursor.execute('''
    CREATE TABLE Instances (id SERIAL PRIMARY KEY, book_id INT REFERENCES book(id), place_id INT REFERENCES book_depository(id));
               ''')
cursor.execute('''
    CREATE TABLE book_author (book_id INT REFERENCES book(id), author_id INT REFERENCES author(id));
               ''')


cursor.execute('''
    INSERT INTO Book (name, Description)
    VALUES
        ('Математика 6 класс', 'Учебник' ),
        ('Отцы и дети', 'Тут нет никакого описания'),
        ('Ася', 'Я не смог придумать'),
        ('Евгений Онегин', 'Роман'),
        ('Русский язык 6 класс', 'Учебник' ),
        ('Сказка о рыбаке и рыбаке', 'Сказка'),
        ('Капитанская дочка', 'Действие происходит во время восстания Емельяна Пугачёва.'),
        ('Герой нашего времени', '1837 год: еще один год изнурительной кавказской войны...'),
        ('Мертвые души', 'Это произведение не о том что ты думаешь'),
        ( 'Миргород', 'Сборник'),
        ( 'Идиот', 'Я не читал, а искать лень');
               ''')

cursor.execute('''
    INSERT INTO Author (FIO)
    VALUES
        ('Львов Валентин Витальевич'),
        ('Наум Яковлевич Виленкин'),
        ('Владимир Иванович Жохов'),
        ('Чесноков Александр Семёнович'),
        ('Львова Светлана Ивановна'),
        ('Иваан Сергееевич Тургенев'),
        ('Пушкин Александр Сереевич'),
        ('Лермонтов Михаил Юрьевич'),
        ('Гоголь Николай Васильевич'),
        ('Достоевский Фёдор Михайлович');
               ''')

cursor.execute('''
    INSERT INTO book_depository (name, place)
    VALUES
        ('Центральная Библиотека', 'Ленина д.15'),
        ('Библиотека имени Гайдара', 'Пушкина д.24'),
        ('Библиотека имени Пушкина', 'Ербанова д.15'),
        ('Национальная Библиотека', 'проспект Победы д.17'),
        ('Национальная Библиотека', 'проспект Победы д.8'),
        ('Республиканская Библиотека', 'бульвар Карла-Маркса д.18'),
        ('Детская Библиотека', 'Ключевская д.13'),
        ('Юнешская Библиотека', 'Геологическая д.23'),
        ('Библиотека имени Калашникова', 'проспект Строитнелей д.27'),
        ('Научная Библиотека', 'Ербанова д.79');
     ''')


cursor.execute('''
    INSERT INTO book_author (book_id, author_id)
    VALUES
               ((SELECT id FROM book WHERE name = 'Русский язык 6 класс') ,              
                        (SELECT id FROM author WHERE fio ='Львова Светлана Ивановна' ) ),
               
               ((SELECT id FROM book WHERE name ='Русский язык 6 класс') ,           
                        (SELECT id FROM author WHERE fio ='Львова Светлана Ивановна' ) ),
               
               ((SELECT id FROM book WHERE name ='Математика 6 класс') ,          
                        (SELECT id FROM author WHERE fio ='Наум Яковлевич Виленкин' ) ),
               
               ((SELECT id FROM book WHERE name ='Математика 6 класс') ,          
                        (SELECT id FROM author WHERE fio ='Владимир Иванович Жохов' ) ),
               
               ((SELECT id FROM book WHERE name ='Математика 6 класс') , 
                        (SELECT id FROM author WHERE fio ='Чесноков Александр Семёнович' ) ),
               
               ((SELECT id FROM book WHERE name ='Отцы и дети') , 
                        (SELECT id FROM author WHERE fio ='Иваан Сергееевич Тургенев' ) ),
               
               ((SELECT id FROM book WHERE name ='Ася') , 
                        (SELECT id FROM author WHERE fio ='Иваан Сергееевич Тургенев' ) ),
               
               ((SELECT id FROM book WHERE name ='Евгений Онегин') , 
                        (SELECT id FROM author WHERE fio ='Пушкин Александр Сереевич' ) ),
               
               ((SELECT id FROM book WHERE name ='Сказка о рыбаке и рыбаке') , 
                        (SELECT id FROM author WHERE fio ='Пушкин Александр Сереевич' ) ),
               
               ((SELECT id FROM book WHERE name ='Капитанская дочка') , 
                        (SELECT id FROM author WHERE fio ='Пушкин Александр Сереевич' ) ),
               
               ((SELECT id FROM book WHERE name ='Герой нашего времени') , 
                        (SELECT id FROM author WHERE fio = 'Лермонтов Михаил Юрьевич' ) ),
               
               ((SELECT id FROM book WHERE name ='Мертвые души') , 
                        (SELECT id FROM author WHERE fio ='Гоголь Николай Васильевич' ) ),
               
               ((SELECT id FROM book WHERE name ='Миргород') , 
                        (SELECT id FROM author WHERE fio ='Достоевский Фёдор Михайлович' ) ),
               
               ((SELECT id FROM book WHERE name ='Идиот') , 
                        (SELECT id FROM author WHERE fio ='Достоевский Фёдор Михайлович' ) );
               
                ''')


cursor.execute('''
    INSERT INTO Instances (book_id, place_id)
    VALUES
               ((SELECT id FROM book WHERE name = 'Русский язык 6 класс') ,              
                        (SELECT id FROM book_depository WHERE name ='Центральная Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Русский язык 6 класс') ,           
                        (SELECT id FROM book_depository WHERE name ='Центральная Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Математика 6 класс') ,          
                        (SELECT id FROM book_depository WHERE name ='Библиотека имени Гайдара' ) ),
               
               ((SELECT id FROM book WHERE name ='Математика 6 класс') ,          
                        (SELECT id FROM book_depository WHERE name ='Библиотека имени Пушкина' ) ),
               
               ((SELECT id FROM book WHERE name ='Математика 6 класс') , 
                        (SELECT id FROM book_depository WHERE name ='Национальная Библиотека' LIMIT 1) ),
               
               ((SELECT id FROM book WHERE name ='Отцы и дети') , 
                        (SELECT id FROM book_depository WHERE name ='Республиканская Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Ася') , 
                        (SELECT id FROM book_depository WHERE name ='Детская Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Евгений Онегин') , 
                        (SELECT id FROM book_depository WHERE name ='Детская Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Сказка о рыбаке и рыбаке') , 
                        (SELECT id FROM book_depository WHERE name ='Юнешская Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Капитанская дочка') , 
                        (SELECT id FROM book_depository WHERE name ='Библиотека имени Калашникова' ) ),
               
               ((SELECT id FROM book WHERE name ='Герой нашего времени') , 
                        (SELECT id FROM book_depository WHERE name = 'Библиотека имени Калашникова' ) ),
               
               ((SELECT id FROM book WHERE name ='Мертвые души') , 
                        (SELECT id FROM book_depository WHERE name ='Научная Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Миргород') , 
                        (SELECT id FROM book_depository WHERE name ='Научная Библиотека' ) ),
               
               ((SELECT id FROM book WHERE name ='Идиот') , 
                        (SELECT id FROM book_depository WHERE name ='Научная Библиотека' ) );
               
                ''')



conn.commit()
cursor.close()
conn.close()