/* SELECT*/
-- SELECT name, price,date FROM product ORDER BY date DESC;
-- SELECT name, city FROM customer WHERE city='Lublin';
-- SELECT *FROM product;
/* DELETE*/
-- DELETE name FROM customer WHERE city="Lublin" name='Katarzyna';
-- DELETE FROM product WHERE price>'20'; 
-- SELECT * FROM product WHERE price>'20'; 
/* INSERT */
-- INSERT INTO tabela VALUES (wartość,wartość2,wartość..);
-- INSERT INTO Product VALUES (10,'Apaszka',35, 2);
-- SELECT * FROM product;
-- INSERT INTO Product VALUES (8,'Kapelusz',60.000000000, 4, '28-01-2020');
-- SELECT * FROM product;
--  DELETE FROM product WHERE date='28-01-2020'; 
--  SELECT * FROM product;
/*UPDATE */
-- UPDATE jakaś tabela SET kolumna=,kolumna= WHERE wartość=;
-- UPDATE jaka tabela SET kolumna=,kolumna= WHERE wartość=;
/*CREATE DATABASE */
-- CREATE DATABASE nazwa bazy - tworzenie bazy*/
/*DROP DATABASE nazwa bazy - usuwanie całej bazy*/
/*CREATE TABLE  nazwa tabeli (nazwa kolumny typ (długość) NOT NULL <- not null nie godzimy się na brak wartości*/
-- UNSIGNED - jesli pole jest liczba to musi być nieujemna
-- RIMERY KEY - kolumna bedzie kluczem podstawowym tabeliSQL AUTO INCREMENT
-- CREATE TABLE 
/*DROP TABLE nazwa tabeli; drop table usuwa zawartość oraz definicje tabeli  */
-- DROP TABLE Product;
-- SELECT * FROM product; <- wywala bląd bo usuneliśmy całą tabele wraz z jej zawartością
-- SELECT * FROM Customer;
-- DELETE FROM Customer; /* usuneliśmy zawartość tabeli */
-- SELECT * FROM Customer;
-- /*CREATE TABLE */
-- CREATE TABLE "Product" (
-- 	"id"		SMALLINT UNSIGNED IDENTITY (1,1) NOT NULL, /* identyty ok którego miejsca startujemy i o ile się przesówamy */
-- ame" 	VARCHAR(50) NOT NULL,
-- 	"price" 	FLOAT NOT NULL,
-- 	"amount" TINYINT (2) NOT NULL,
-- 	PRIMARY KEY ("id")
-- );
-- SELECT * FROM product;

/* ROZBUDOWA SELECT WHERE */
-- SELECT * FROM * WHERE /* AND OR NOT warunki klasyczne */
-- SELECT * FROM Customer;
-- SELECT id, name, city, date FROM Customer WHERE name="Katarzyna" AND city="Lublin";
-- SELECT * FROM Product;
-- SELECT * FROM Product WHERE price>25 OR amount >=5;

-- /* OPERATOR LIKE */
-- SELECT * FROM customer;
-- SELECT id, name,city,date FROM Customer WHERE name LIKE 'm%'; /nie interesuje go wielkość liter i procent daje dowolną ilość znaków

-- SELECT id, name, price FROM Product WHERE name LIKE "%a%"; / _ podkreślenie zastepuje jeden znak

-- /* OPERATOR IN */
-- SELECT kolumna,kolumna FROM tabelea WHERE kolumna IN (element zbiór wartości)
-- SELECT name, price FROM Product WHERE price IN (60,10,25)

-- SELECT name, price, amount FROM Product WHERE amount IN (3,4,5,6)

-- /* OPERATOR BETWEEN */
--  SELECT name, price FROM Product WHERE price BETWEEN 40 AND 60; /* przedziały obustronnie zamkniete*/
-- 
-- /* OPERATOR IS NULL*/ pomaga wyciągnąć nulle - przydaje się jesli pozwoliliśmy na coś takiego to wyciągamy takie wiersze
-- SELECT kolumna,kolumna FROM talebe WHERE kolumna IS NULL /*lub not null*/

--/* KLAUZULA TOP */ "SELECT TOP" "SELECT TOP x PERCENT" w MySQL jest zamiast tego LIMIT na końcu

-- SELECT id, name, price FROM Product WHERE price>20 LIMIT 1; /* wyrzuca tylko spodnie bo jest limit 1
 SELECT id, name FROM Customer LIMIT 4;  /* bez warunku tylko top 4 klientów
 