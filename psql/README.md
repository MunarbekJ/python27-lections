# Slash commands
* \l - список всех бд
* \c - показывает через какого юзера и к какой бд мы подключены
* \c name_of_db - подключение к какой-то бд
* \du - список всех юзеров в postges
* \dt - список всех таблиц в текущей бд
* \d+ - более подробная информация о таблицах в текущей бд
* \d+ name_of_table - более подробная информация о таблице
* \q - выход из субд (psql)


# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создание бд
```

```sql
CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2,
    ...
);
-- создание таблицы с полями
```

# Удаление бд и таблиц
```sql
DROP DATABASE name_of_db;
-- удаление бд
```

```sql
DROP TABLE name_of_table;
-- удаление таблицы
```

# Заполнение таблиц
```sql
INSERT INTO name_of_db VALUES
(val1, val2),
(val1.2, val2.2);
-- запись данных в таблицу (заполнение всех полей)
```

# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- вывод всех записей со всеми полями
```

```sql
SELECT column1, column3 FROM name_of_table;
-- вывод конкретных полей
```

# Условия
```sql
DELETE FROM name_of_table WHERE condition;
-- удаление всех записей из таблицы соответствующих данному условию
```
CREATE TABLE author (
    id serial PRIMARY KEY,
    name varchar(50),
    last_name varchar(70)
);

CREATE TABLE authobiography (
    id serial PRIMARY KEY, published date,
    body text,
    author_id int UNIQUE, -- чтобы создать one - one , добавляем unique

CONSTRAINT fk_author_bio

);
## реализация many2many postgres
```sql

CREATE TABLE developer (
    id serial PRIMARY KEY,
    name varchar(50),
    age int,
    experience int
);

CREATE TABLE project (
    id serial PRIMARY KEY,
    title varchar(100),
    tz text,
    deadline date
);

CREATE TABLE dev_proj (
    dev_id int,
    proj_id int,

    CONSTRAINT fk_dev_m2m
    FOREIGN KEY (dev_id) REFERENCES developer (id),

    CONSTRAINT fk_proj_m2m
    FOREIGN KEY (proj_id) REFERENCES project (id)
);


```

```sql
SELECT * FROM blogger
JOIN post ON blogger.id = post.blogger_id;


```
```sql
SELECT *FROM developer
JOIN dev_proj ON  developer.id = dev_proj.dev_id
JOIN project ON project.id = dev_proj.proj_id;
```

# Агрегатные функции 
> все агрегатные функции используется с 'group by'
```psql
> **SUM** - СЧИТАЕТ СУММУ ВСЕХ ЗАПИСЕЙ В ГРУППИРОВАННЫМ ПОЛЕ

 SELECT customer.name, SUM(product.price)
FROM customer
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id);
-- name    | round 
------------+-------
 customer 2 |   470
 customer 3 |   344
 customer 1 |   360
(3 rows)



>**AVG** - считает среднее значение всех записей в сгрупироонаным поле
SELECT customer.name, AVG(product.price)
FROM customer
JOIN cart ON customer.id = cart.customer_id
JOIN product ON product.id = cart.product_id
GROUP BY (customer.id);
   name    | round  
------------+--------
 customer 2 | 470.00
 customer 3 | 344.00
 customer 1 | 359.67
 name    |         avg          
------------+----------------------
 customer 2 | 470.0000000000000000
 customer 3 | 344.0000000000000000
 customer 1 | 359.6666666666666667
```
> **ARRAY_AGG** - СОБИРАЕТ ЗНАЧЕНИЕ ВСЕХ ЗАПИСЕЙ В СГРУППИРОВАННЫМ ПОЛЕ 

>**MIN/MAX** - ВЫБИРАЕТ МИНИМАЛЬНОЕ .МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ ИЗ ВСЕХ ЗАПИСЕЙ В СГРУППИРОВАННЫОМ ПОЛЕ
SELECT blogger.name,MIN(post.body) FROM blogger
JOIN post on blogger.id = post.blogger_id 
GROUP BY (blogger.id);
   name    |        min         
-----------+--------------------
 blogger 2 | my first post
 blogger 3 | i am not a blogger
 blogger 1 | it is my b-day!

 SELECT blogger.name,MAX(post.body) FROM blogger
JOIN post on blogger.id = post.blogger_id 
GROUP BY (blogger.id);
   name    |         max         
-----------+---------------------
 blogger 2 | some post
 blogger 3 | i am not a blogger
 blogger 1 | today is a good day



>**COUNT**
```sql
 SELECT blogger.name,COUNT(post.body) FROM blogger
JOIN post on blogger.id = post.blogger_id 
GROUP BY (blogger.id);
   name    | count 
-----------+-------
 blogger 2 |     4
 blogger 3 |     2
 blogger 1 |     6
(3 rows)



```
# Import/Export баз данных

write from file to db
```bash
psql db_name < file.sql
# при этом db_name  должно существовать 
```
write from db to file
```bash
pg_dump db_name > file.sql
```
