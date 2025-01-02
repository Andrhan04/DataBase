"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
    CREATE TABLE Book (id SERIAL PRIMARY KEY, name TEXT NOT NULL CHECK (TRIM(name) = '' IS NOT TRUE), Description TEXT NOT NULL);
    CREATE TABLE author (id SERIAL PRIMARY KEY, fio TEXT NOT NULL CHECK (TRIM(fio) = '' IS NOT TRUE) UNIQUE);
    CREATE TABLE book_depository (id SERIAL PRIMARY KEY, name TEXT NOT NULL CHECK (TRIM(name) = '' IS NOT TRUE), place TEXT NOT NULL CHECK (TRIM(place) = '' IS NOT TRUE));
    CREATE TABLE Instances (id SERIAL PRIMARY KEY, book_id INT REFERENCES book(id) ON DELETE CASCADE, place_id INT REFERENCES book_depository(id) ON DELETE CASCADE);
    CREATE TABLE book_author (book_id INT REFERENCES book(id) ON DELETE CASCADE, author_id INT REFERENCES author(id) ON DELETE CASCADE);
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
    step("""
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
               
                """),
    step('''
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
               
                '''),
                step("""
                     SELECT setval('book_depository_id_seq', (SELECT max(id)+1 FROM book_depository));
                     SELECT setval('book_id_seq', (SELECT max(id)+1 FROM book));
                     SELECT setval('author_id_seq', (SELECT max(id)+1 FROM author));

                     """),
#------------------------------------------------------------------------
    step("""
        DROP FUNCTION IF EXISTS get_all();
        CREATE OR REPLACE FUNCTION get_all()
        RETURNS TABLE(id INT, name TEXT) AS $$
        BEGIN
            RETURN QUERY
                SELECT author.id, author.fio
                FROM author  ORDER BY id;
        END;
        $$ LANGUAGE plpgsql;
    """),

     step("""
        DROP FUNCTION IF EXISTS get(TEXT);
        CREATE OR REPLACE FUNCTION get(IN cur_user_id TEXT)
        RETURNS TABLE(id INT, fio TEXT) AS $$
        DECLARE
            cur_id INT;
        BEGIN
            cur_user_id := TRIM(cur_user_id);
            IF LENGTH(cur_user_id) = 0 OR NOT cur_user_id ~ '^[0-9]+$' OR (cur_user_id = '0') THEN
                RAISE EXCEPTION 'The identifier must be a positive integer and cannot be empty';
            END IF;
            cur_id := CAST(cur_user_id AS INT);
            IF NOT EXISTS (SELECT 1 FROM author WHERE author.id = cur_id) THEN
                RAISE EXCEPTION 'Author with ID % not found', cur_id;
            END IF;
            
            RETURN QUERY SELECT author.id, author.fio  FROM author WHERE author.id = cur_id;
        END;
        $$ LANGUAGE plpgsql;
    """),

    step('''
        DROP FUNCTION IF EXISTS delete_many(TEXT[]);
        CREATE OR REPLACE FUNCTION delete_many(cur_user_id TEXT[])
        RETURNS INTEGER AS $$
        DECLARE
            cur_id INT;
            deleted_count INT := 0; 
            id TEXT; 
        BEGIN
            FOREACH id IN ARRAY cur_user_id LOOP
                IF id IS NULL OR NOT id ~ '^[0-9]+$' THEN
                    RAISE NOTICE 'ID % is not valid.', id;
                    CONTINUE; 
                END IF;
                cur_id := id::INT;
                IF EXISTS (SELECT 1 FROM author WHERE author.id = cur_id) THEN
                    DELETE FROM author WHERE author.id = cur_id;
                    deleted_count := deleted_count + 1;  
                ELSE
                    RAISE NOTICE 'The author with ID % was not found.', cur_id;
                END IF;
            END LOOP;
            RAISE NOTICE 'Removed Author: %', deleted_count;
            RETURN deleted_count;  
        END;
        $$ LANGUAGE plpgsql;
    '''),

    step('''
        DROP PROCEDURE IF EXISTS delete(TEXT);
        CREATE OR REPLACE PROCEDURE delete(IN cur_user_id TEXT)
        LANGUAGE plpgsql AS $$
        DECLARE
            cur_id INT;
        BEGIN
            cur_id := NULLIF(TRIM(cur_user_id), '');
            IF cur_id IS NULL OR NOT (cur_user_id ~ '^[0-9]+$') OR (cur_user_id = '0') THEN
                RAISE EXCEPTION 'The author id must be a positive integer and cannot be empty';
            END IF;
            cur_id := CAST(cur_id AS INT);

            IF NOT EXISTS (SELECT 1 FROM author WHERE id = cur_id) THEN
                RAISE EXCEPTION 'Author with ID % not found', cur_id;
            END IF;
            DELETE FROM author WHERE id = cur_id;
        END;
        $$;
    '''),

    step('''
    DROP PROCEDURE IF EXISTS update(TEXT,TEXT);
    CREATE OR REPLACE PROCEDURE update (
        IN cur_id TEXT, 
        IN cur_name TEXT
    )
    LANGUAGE plpgsql AS $$
    BEGIN
        IF LENGTH(cur_id) = 0 OR NOT cur_id ~ '^[0-9]+$' THEN
            RAISE EXCEPTION 'The author id must be a positive integer and cannot be empty ';
        END IF;
        DECLARE
            cur_id INT := CAST(cur_id AS INT);
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM author WHERE author.id = cur_id) THEN
                RAISE EXCEPTION 'author with ID % not found', cur_id;
            END IF;
            IF cur_name IS NOT NULL AND cur_name <> '' THEN                
                UPDATE author 
                SET fio = cur_name
                WHERE author.id = cur_id;
            END IF;
        END;
    END;
    $$;
    '''),


    step('''
    DROP PROCEDURE IF EXISTS add(TEXT);
    CREATE OR REPLACE PROCEDURE add(
        IN cur_name TEXT
    )
    LANGUAGE plpgsql AS $$
    BEGIN
        IF LENGTH(cur_name) = 0 THEN
            RAISE EXCEPTION 'Name cannot be empty or consist only of spaces';
        END IF;
        INSERT INTO author (fio) 
        VALUES (cur_name);
    END;
    $$;
         '''),
    
#-----------------------------------------------------------------------------------------
    step(
        '''
            DROP TRIGGER IF EXISTS name_trigger ON Author;
        '''
    ),

    step(
        '''
            DROP FUNCTION IF EXISTS name_validate();
        '''
   ),
    step(
        '''
            CREATE OR REPLACE FUNCTION name_validate()
            RETURNS trigger
            LANGUAGE plpgsql
            AS $$
            BEGIN
                NEW.fio = replace(NEW.fio, '\', '');
                NEW.fio = replace(NEW.fio, '!', '');
                NEW.fio = replace(NEW.fio, '@', '');
                NEW.fio = replace(NEW.fio, '#', '');
                NEW.fio = replace(NEW.fio, '$', '');
                NEW.fio = replace(NEW.fio, '^', '');
                NEW.fio = replace(NEW.fio, ':', '');
                NEW.fio = replace(NEW.fio, '.', '');
                NEW.fio = replace(NEW.fio, ',', '');
                NEW.fio = replace(NEW.fio, '/', '');
                NEW.fio = replace(NEW.fio, '&', '');
                NEW.fio = replace(NEW.fio, '*', '');
                NEW.fio = replace(NEW.fio, '(', '');
                NEW.fio = replace(NEW.fio, ')', '');
                NEW.fio = replace(NEW.fio, '[', '');
                NEW.fio = replace(NEW.fio, ']', '');
                NEW.fio = replace(NEW.fio, '{', '');
                NEW.fio = replace(NEW.fio, '}', '');

                NEW.fio = regexp_replace(NEW.fio,'[^A-Za-zа-яА-ЯёЁ]+$]','','g');
                NEW.fio = INITCAP(TRIM(regexp_replace(NEW.fio, '\s+', ' ', 'g')));
                RETURN NEW;
            END;
            $$;
        '''
    ),
    step(
        '''
            CREATE TRIGGER name_trigger
            BEFORE INSERT OR UPDATE ON Author
            FOR EACH ROW EXECUTE FUNCTION name_validate();
        '''
    )
]
