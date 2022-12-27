INSERT INTO translator(full_name, age, education)
VALUES
    ('В.В. Грибник', 40,'Высшее в МГУ'),
    ('И.П. Черкасов', 42,'Среднее общее'),
    ('В.Г. Чиж', 56,'Высшее в ВШЭ'),
    ('А.Ф. Гриб', 34,'Высшее в МГПУ'),
    ('К.К. Грик', 27, 'Высшее в МАИ'),
    ('Ф.М. Дриб', 60, 'Среднее профессиональное');

INSERT INTO printing_house(name, address)
VALUES
    ('Астрель','г. Москва, ул. Петровская, д.10'),
    ('Печатники','г. Клин, ул. Петровкая, д.11'),
    ('Книжник','г. Новосибирск, ул. Первая, д.15'),
    ('Типография','г. Москва, ул. Майская, д.4');


INSERT INTO editor_in_chief(full_name, age)
VALUES
    ('И.В. Игнатов', 45),
    ('И.К. Игов', 48),
    ('П.В. Липатов', 54),
    ('В.К. Кант', 39);

INSERT INTO publication(name, genre, origin_language, editor_id)
VALUES
    ('Name 1', 'Фантастика', 'Русский', 2),
    ('Name 2', 'Фантастика', 'Английский', 3),
    ('Name 3', 'Драма', 'Испанский', 4),
    ('Name 4', 'Проза', 'Русский', 4),
    ('Name 5', 'Лирика', 'Испанский', 4),
    ('Name 6', 'Комедия', 'Английский', 3),
    ('Name 7', 'Роман', 'Русский', 2),
    ('Name 8', 'Роман', 'Русский', 2),
    ('Name 9', 'Фантастика', 'Русский', 4),
    ('Name 10', 'Поэма', 'Русский', 4);


INSERT INTO translations(publication_id, translator_id)
VALUES
    (2,2),
    (3,2),
    (5,3),
    (6,6);


INSERT INTO publisher(name, world_rating, address)
VALUES
    ('Лучшее издательство', 9,'Лучшее место в мире');


INSERT INTO advertising_agency(name, address, rating)
VALUES
    ('Рекламное агенство 1','Адрес 1',7),
    ('Рекламное агенство 2','Адрес 2',8),
    ('Рекламное агенство 3','Адрес 3',9);


INSERT INTO advertising_publisher(agency_id, publisher_id)
VALUES
    (1,1),
    (2,1),
    (3,1);

INSERT INTO agent(full_name, age, phone_number, publisher_id)
VALUES
    ('Тестовый',42,'+71111111',1);


INSERT INTO author(full_name, agent_id)
VALUES
    ('П.А. Первый',1),
    ('В.А. Второй',2),
    ('Т.А. Третий',3),
    ('Ч.А. Четвертый',1);

INSERT INTO author_publication(author_id, publication_id)
VALUES
    (1,7),
    (1,8),
    (1,9),
    (1,10),
    (2,1),
    (2,4),
    (3,3),
    (3,5),
    (4,2),
    (4,6);

INSERT INTO edition(amount, edition_type, publication_id, printing_house_id)
    VALUES
    (10000,'Коллекционное',1, 1),
    (15000,'Подарочное',2, 3),
    (10000,'Коллекционное',3, 2),
    (5000,'Обычное',4, 2),
    (1000,'Эксклюзивное',5, 3),
    (20000,'Обычное',6, 4),
    (30000,'Обычное',7, 4),
    (15000,'Подарочное',8, 1),
    (10000,'Юбилейное',9, 2),
    (5000,'Обычное',10, 3);
