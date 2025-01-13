"""
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
    CREATE TABLE Book (id SERIAL PRIMARY KEY, name TEXT NOT NULL CHECK (TRIM(name) = '' IS NOT TRUE), Description TEXT NOT NULL, del BOOLEAN DEFAULT FALSE);
    CREATE TABLE author (id SERIAL PRIMARY KEY, fio TEXT NOT NULL CHECK (TRIM(fio) = '' IS NOT TRUE) UNIQUE, del BOOLEAN DEFAULT FALSE);
    CREATE TABLE book_depository (id SERIAL PRIMARY KEY, name TEXT NOT NULL CHECK (TRIM(name) = '' IS NOT TRUE), place TEXT NOT NULL CHECK (TRIM(place) = '' IS NOT TRUE), del BOOLEAN DEFAULT FALSE);
    CREATE TABLE Instances (id SERIAL PRIMARY KEY, book_id INT REFERENCES book(id) ON DELETE CASCADE, place_id INT REFERENCES book_depository(id) ON DELETE CASCADE, del BOOLEAN DEFAULT FALSE);
    CREATE TABLE book_author (book_id INT REFERENCES book(id) ON DELETE CASCADE, author_id INT REFERENCES author(id) ON DELETE CASCADE, del BOOLEAN DEFAULT FALSE );
"""),
    step("""
    INSERT INTO Book (id,name, Description)
    VALUES
        (1,'Математика 6 класс', 'Учебник' ),
        (2,'Отцы и дети', 'Тут нет никакого описания'),
        (3,'Ася', 'Я не смог придумать'),
        (4,'Евгений Онегин', 'Роман'),
        (5,'Русский язык 6 класс', 'Учебник' ),
        (6,'Сказка о рыбаке и рыбаке', 'Сказка'),
        (7,'Капитанская дочка', 'Действие происходит во время восстания Емельяна Пугачёва.'),
        (8,'Герой нашего времени', '1837 год: еще один год изнурительной кавказской войны...'),
        (9,'Мертвые души', 'Это произведение не о том что ты думаешь'),
        (10, 'Миргород', 'Сборник'),
        (11, 'Идиот', 'Я не читал, а искать лень');
"""),
    step("""
        INSERT INTO Author (id,FIO)
            VALUES
                (1,'Львов Валентин Витальевич'),
                (2,'Наум Яковлевич Виленкин'),
                (3,'Владимир Иванович Жохов'),
                (4,'Чесноков Александр Семёнович'),
                (5,'Львова Светлана Ивановна'),
                (6,'Иваан Сергееевич Тургенев'),
                (7,'Пушкин Александр Сереевич'),
                (8,'Лермонтов Михаил Юрьевич'),
                (9,'Гоголь Николай Васильевич'),
                (10,'Достоевский Фёдор Михайлович');
"""),
    step("""
    INSERT INTO book_depository (id,name, place)
    VALUES
        (1,'Центральная Библиотека', 'Ленина д.15'),
        (2,'Библиотека имени Гайдара', 'Пушкина д.24'),
        (3,'Библиотека имени Пушкина', 'Ербанова д.15'),
        (4,'Национальная Библиотека', 'проспект Победы д.17'),
        (5,'Национальная Библиотека', 'проспект Победы д.8'),
        (6,'Республиканская Библиотека', 'бульвар Карла-Маркса д.18'),
        (7,'Детская Библиотека', 'Ключевская д.13'),
        (8,'Юнешская Библиотека', 'Геологическая д.23'),
        (9,'Библиотека имени Калашникова', 'проспект Строитнелей д.27'),
        (10,'Научная Библиотека', 'Ербанова д.79');
"""),
     step('''
        INSERT INTO Instances (book_id, place_id)
            VALUES
                (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), 
                (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10);
'''),
step("""
         INSERT INTO book_author (book_id, author_id)
            VALUES
                (1,1),(1,2),(2,3),(2,4),(2,5),
                (3,6),(4,6),(5,7),(6,7),(7,7),
                (8,8),(9,9),(10,9),(11,10);
"""),
    step("""
        SELECT setval('book_depository_id_seq', (SELECT max(id)+1 FROM book_depository));
        SELECT setval('book_id_seq', (SELECT max(id)+1 FROM book));
        SELECT setval('author_id_seq', (SELECT max(id)+1 FROM author));
        SELECT setval('Instances_id_seq', (SELECT max(id)+1 FROM Instances));
"""),
    step("""
        CREATE OR REPLACE FUNCTION soft_delete()
        RETURNS TRIGGER AS $$
        BEGIN
            -- Обновляем запись: устанавливаем is_active в false и deleted_at в текущее время
            UPDATE book_depository
            SET del = true
            WHERE book_depository.id = OLD.id;
            -- Отменяем DELETE, возвращая NULL
            RETURN NULL;
        END;
        $$ LANGUAGE plpgsql;
"""),
    step("""
        CREATE TRIGGER soft_delete_book_trigger
        BEFORE DELETE ON book_depository
        FOR EACH ROW
        EXECUTE FUNCTION soft_delete();
""")
]
