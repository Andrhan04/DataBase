'''
step("CREATE TABLE tanks (id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, parent_id INTEGER REFERENCES tanks(id) ON DELETE CASCADE, name VARCHAR(255) NOT NULL)",
         "DROP TABLE tanks"),
    step("""
         INSERT INTO tanks (id, parent_id, name) VALUES
         (1,NULL,'Наземная техника'),
         (2,1,'САУ'),
               (7,2,'Артилерия'),
                         (20,7,СУ-8'),
                         (21,7,СУ-14-1'),
                         
               (8,2,'ПТ-САУ'),
                         (9,8,'oбъект-268'),
                         (10,8,'ИСУ 152'),
         (3,1,'Танк'),
               (4,3,'легкие'),
                         (14,4,'МС-1'),
                         (15,4,'Valentine'),
                         (16,4,'БТ'),
                         (19,4,'Т-26'),
               (5,3,'средние'),
                         (17,5,'Т-34'),
                         (18,5,' Pz.Kpfw. V Panther'),
               (6,3,'тяжелые'),
                         (11,6,'ИС-1'),
                         (12,6,'КВ-1'),
                         (13,6,'Pz.Kpfw. VI Tiger')
         """)
'''