CREATE TABLE IF NOT EXISTS publisher
(
    publisher_id serial PRIMARY KEY NOT NULL,
    name varchar(30) not null,
    world_rating INT NOT NULL,
    address VARCHAR(50) NOT NULL
);

CREATE TABLE if not exists editor_in_chief
(
    editor_id serial primary key not null,
    full_name varchar (50) not null,
    age int not null
);

CREATE TABLE IF NOT EXISTS publication
(
    publication_id serial primary key not null,
    name varchar(20) not null,
    genre varchar(100) not null,
    origin_language varchar(50) not null,
    editor_id int references editor_in_chief(editor_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS translator
(
    translator_id serial primary key not null,
    full_name varchar (50) not null,
    age int not null,
    education varchar (100) not null
);

CREATE TABLE IF NOT EXISTS translations
(
    publication_id INT not null REFERENCES publication(publication_id) ON DELETE CASCADE,
    translator_id int not null REFERENCES translator(translator_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS agent
(
    agent_id serial primary key not null,
    full_name varchar(50) NOT NULL,
    age int not null,
    phone_number varchar(20) not null,
    publisher_id int not null references publisher(publisher_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS author
(
  author_id serial PRIMARY KEY not null,
  full_name varchar (50) not null,
  agent_id int references agent(agent_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS author_publication
(
    author_id int not null REFERENCES author(author_id) ON DELETE CASCADE,
    publication_id int not null REFERENCES publication(publication_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS printing_house
(
    printing_house_id serial PRIMARY KEY not null,
    name varchar(30) NOT NULL,
    address varchar(50) NOT NULL
);

CREATE TABLE if not exists advertising_agency
(
    agency_id serial primary key not null,
    name varchar(30) NOT NULL,
    address varchar(50) NOT NULL,
    rating int NOT NULL
);

CREATE TABLE if not exists advertising_publisher
(
    agency_id int references advertising_agency(agency_id) ON DELETE CASCADE,
    publisher_id int references publisher(publisher_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS edition
(
    edition_id serial primary key not null,
    amount int not null,
    edition_type varchar(30) not null,
    publication_id int not null REFERENCES publication(publication_id) ON DELETE CASCADE,
    printing_house_id int not null REFERENCES printing_house(printing_house_id) ON DELETE CASCADE
);

create or replace function phone_check() returns trigger as $psql$
    declare num varchar(15);

    begin
        num = new.phone_number;
        if (num not like '+7%') then
            RAISE EXCEPTION 'Wrong number format!';
        end if;
        return new;
    end;
$psql$ language plpgsql;


create trigger phone_check before insert on agent
for each row execute procedure phone_check();


create view publication_view as
    select publication.name as Название, publication.genre as Жанр, publication.origin_language as Язык_оригинала,
           editor_in_chief.full_name as ФИО_Редактора from publication
join author_publication on publication.publication_id = author_publication.publication_id
               join editor_in_chief on editor_in_chief.editor_id = publication.editor_id
    join author on author_publication.author_id = author.author_id;












select publication.name, publication.genre, publication.origin_language, editor_in_chief.full_name from publication
join author_publication on publication.publication_id = author_publication.publication_id join editor_in_chief on editor_in_chief.editor_id = publication.editor_id
    join author on author_publication.author_id = author.author_id;

select edition.amount, edition.edition_type, publication.name, publication.genre, author.full_name
from edition, publication,author, author_publication where edition.publication_id = publication.publication_id
                                                       and author_publication.publication_id = publication.publication_id
                                                       and author.author_id = author_publication.author_id;

select translator.full_name, translator.age, translator.education from translator;

select publication.name from publication join edition on publication.publication_id = edition.publication_id;

select edition.edition_id from edition

--where publication.publication_id = author_publication.publication_id and author_publication.author_id = 1

















