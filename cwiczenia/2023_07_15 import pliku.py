#import sqlite3
# conn = sqlite3.connect('example.db')
#
# c = conn.cursor() # tworzymy kursor
#
# #tworzymy coś na obiekcie poprzez execute możemy to zrobić tylko raz
# c.execute(('''CREATE TABLE if not exists stocks
#              (date text, trans text, symbol text, qty real, price real)'''))
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# conn.commit() #commitowanie połączenia
# conn.close() #zamykanie połączenia

# conn = sqlite3.connect('example.db') #łączymy się do bazy - jesli jest stworzona to pracujemy na bazie
# c = conn.cursor() # tworzymy kursor
# symbol = "RHAT"
# query = f"SELECT * FROM stocks WHERE symbol = '{symbol}';" #tak się nie łaczymy bo jest to niebezpieczne - dajemy cały dostep do bazy komuś
# print(query)
# c.execute(query)
#
# t = ('RHAT', )
# c.execute('SELECT * FROM stocks WHERE symbol=?', t) ##poprawne zapytanie do bazy
# print(c.fetchone()) # zapytanie o jeden element
#
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases) #wiele wierszy wywołanie - jest jeszcze fetchall - wyswietla wszystko
#
# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#     print(row)

#METODA ITERDUMP zwraca wartośc w postaci tekstowej i wrzuca ją do pamięci podręcznej
# kopie zapasowe jak wykonać
# import sqlite3
# import io
# conn = sqlite3.connect('CodeBrainers.db')
# with io.open('CodeBrainers_dump.sql', 'w') as f:
#     for line in conn.iterdump():
#         f.write('%s\n' % line)
# print('Kopia zapasowa została wykonana pomyślnie.')
# print('Zapisano jako CodeBrainers_dump.sql')
# conn.close()

#TODO Cwiczenie 1 Napisz program w języku Python, aby utworzyć połączenie bazy danych SQLite z bazą danych znajdującą się w pamięci.

# import sqlite3
# conn = sqlite3.connect(':memory:') #wrzucenie bazy do pamieci podrecznej
# print('Polaczenie nawiazane')
# conn.close()
# print('Zamknieto połaczenie')

#TODO Cwieczenie 2 Napisz program w Pythonie, aby utworzyć bazę danych SQLite w pliku i połączyć się z bazą danych oraz wydrukować wersję bazy danych SQLite i numer wersji modułu sqlite3 w postaci ciągu.
# Funkcja SQLite sqlite_version zwraca ciąg znaków wersji dla uruchomionej biblioteki SQLite.
# Atrybut Pythona sqlite3.version zwraca numer wersji modułu sqlite3 w postaci ciągu. To nie jest wersja biblioteki SQLite!

# import sqlite3
# conn = sqlite3.connect('example2.db')
# c = conn.cursor()
# #tworzenie query
# query = 'SELECT sqlite3.version()'
# c.execute(query) #zapytanie do kursora
# #pobieramy wszystko co tam jest poprzez fetchall
# record = c.fetchall()
# print("Wersja SQL Lite to ", record)
# print("Wersja modułu SQL Lite ", sqlite3.version)
# conn.close()
# ???

# import sqlite3
# conn = sqlite3.connect('example2.db')
# c = conn.cursor()
# query = 'SELECT sqlite_version()'
# c.execute(query)
# version = c.fetchall()
# print('version sqlite to ', version)
# print ('sqlite3 to ', sqlite3.version)
# conn.close()

#TODO Cwieczenie 3 Napisz program w Pythonie, aby utworzyć bazę danych SQLite i połączyć się z bazą danych oraz zabezpieczyć się przed wyjątkami. Wywołaj sztucznie wyjątek, wykonując błędne zapytanie.
# Podpowiedź: wyjątek sqlite3.Error jest to klasa bazowa pozostałych wyjątków w module sqlite3. Jest to zarazem podklasa Exception.

# import sqlite3
# try:
#     conn = sqlite3.connect('example2.db')
#     c = conn.cursor()
#     query = 'SELECT * FROM tabela'
#     c.execute(query)
# except sqlite3.Error as error:
#     print("Błąd połaczenia z bazą danych ", error)
# finally:
#     conn.close()

#TODO Cwieczenie 4 Napisz program w Pythonie, który wyświetli listy zawartości tabel pliku bazy danych SQLite CodeBrainers.

# import sqlite3
# conn = sqlite3.connect('CodeBrainers.db')
# c = conn.cursor()
# query = 'SELECT * FROM product'
# c.execute(query)
# print(c.fetchall())
# query = 'SELECT * FROM customer'
# c.execute(query)
# print(c.fetchall())
# query = 'SELECT * FROM order_product'
# c.execute(query)
# print(c.fetchall())

#alternatywna metoda
# import sqlite3
# conn = sqlite3.connect('CodeBrainers.db')
# c = conn.cursor()
# c.execute('SELECT name FROM sqlite_schema WHERE type="table"') #ściagamy schemat tabeli
# tables = c.fetchall()
# print(tables)
# for table in tables: # tworzymy funkcje i mapujemy wyniki po niej
#     print(f'\n{table[0]}:')
#     c.execute(f"SELECT * FROM {table[0]}")
#     print(c.fetchall())
# conn.close()

#TODO Cwieczenie 5 Napisz program w Pythonie, aby połączyć bazę danych SQLite i utworzyć tabelę w bazie danych:
# Struktura tabeli Users:
# login VARCHAR(8) NOT NULL
# name VARCHAR(40) NOT NULL
# phone_no VARCHAR(15)
# Następnie spróbuj dodać jeden wiersz (np.: 'user', 'Jan Nowak', '1234567890') i go wyświetlić z bazy danych.

# import sqlite3
# conn = sqlite3.connect('User.db')
# c = conn.cursor()
# query = 'CREATE TABLE if not exists Users(login VARCHAR(8) NOT NULL, name VARCHAR(40) NOT NULL, phone_no VARCHAR(15))'
# c.execute(query)
# print('Stworzono tabele')
# query = "INSERT INTO Users VALUES ('user', 'Jan Nowak', '1234567890')"
# c.execute(query)
# print("dodanie nowego rekordu do istniejącej tabeli")
# query = 'SELECT * FROM Users'
# c.execute(query)
# result = c.fetchall()
# print("Wyniki ", result)
# conn.close()

#TODO Cwieczenie 6 Napisz program w Pythonie, który wstawi listę kilku rekordów do podanej tabeli SQLite o kilku kolumnach (jednym poleceniem). Policz liczbę wierszy w danej tabeli SQLite (przed i po wstawieniu wierszy).
# Przykładowe kolumny tabeli:
# id SMALLINT
# name VARCHAR(30)
# city VARCHAR(35)
# Przykładowe rekordy:
# 5001, 'Piotr Nowak',          'Warszawa'
# 5002, 'Anna Kowalska',        'Kraków'
# 5003, 'Krzysztof Wiśniewski', 'Łódź'
# 5004, 'Maria Wójcik',         'Kraków'
# 5005, 'Andrzej Kowalczyk',    'Wrocław'

# import sqlite3
# conn = sqlite3.connect('User1.db')
# c = conn.cursor()
# query = 'CREATE TABLE if not exists Users1(id SMALINT NOT NULL, name VARCHAR(30) NOT NULL, city VARCHAR(35))'
# c.execute(query)
# print('Stworzono tabele')
# query = 'SELECT * FROM Users1'
# c.execute(query)
# wynik = c.fetchall()
# print("Wielkość tabeli wynosi ", len(wynik))
#
# rekordy = [
# (5001, 'Piotr Nowak',          'Warszawa'),
# (5002, 'Anna Kowalska',        'Kraków'),
# (5003, 'Krzysztof Wiśniewski', 'Łódź'),
# (5004, 'Maria Wójcik',         'Kraków'),
# (5005, 'Andrzej Kowalczyk',    'Wrocław')
# ]
# query = "INSERT INTO Users1(id, name, city) VALUES (?,?,?)"
# c.executemany(query, rekordy) #dodajemy rekord ktory ma wiele linijek
# print("Dodanie wartości do tabeli")
# query = 'SELECT * FROM Users1'
# c.execute(query)
# wynik = c.fetchall()
# print("Obecna wielkość tabeli wynosi ", len(wynik))

#TODO Cwieczenie 7 Napisz program w Pythonie, który będzie wstawiał wartości do tabeli z danych wejściowych użytkownika.
# Przykładowe kolumny tabeli:
# id SMALLINT
# name VARCHAR(30)
# city VARCHAR(35)

# import sqlite3
# conn = sqlite3.connect('User2.db') #':memory:' można też zamiast bazy wpisać to w pamięć a potem wrzucić wynik do bazy
# c = conn.cursor()
# query = 'CREATE TABLE if not exists Users2(id SMALINT NOT NULL, name VARCHAR(30) NOT NULL, city VARCHAR(35))'
# c.execute(query)
# print('Stworzono tabele')
# query = 'SELECT * FROM Users2'
# c.execute(query)
# wynik = c.fetchall()
# print("Utworzona tabela ", wynik)
# user_id = input ('Podaj wartość ID ')
# user_name = input ('Podaj wartość name ')
# user_city = input ('Podaj wartość city ')
# query = "INSERT INTO Users2 (id, name, city) VALUES (?,?,?)"
# c.execute(query, (user_id,user_name, user_city))
# query = 'SELECT * FROM Users2'
# c.execute(query)
# wynik = c.fetchall()
# print("Utworzona nowa tabela ", wynik)
# conn.close()

#TODO Cwieczenie 8 Napisz program w Pythonie, aby zaktualizować określoną wartość kolumny w danej tabeli i wybrać/wyświetlić w pętli wszystkie wiersze przed i po aktualizacji tej tabeli.
# Przykładowe kolumny tabeli:
# id SMALLINT
# name VARCHAR(30)
# city VARCHAR(35)
# Przykładowe rekordy:
# 5001, 'Piotr Nowak',          'Warszawa'
# 5002, 'Anna Kowalska',        'Kraków'
# 5003, 'Krzysztof Wiśniewski', 'Łódź'
# 5004, 'Maria Wójcik',         'Kraków'
# 5005, 'Andrzej Kowalczyk',    'Wrocław'

# import sqlite3
# conn = sqlite3.connect(':memory:')
# c = conn.cursor()
# # Utwórz tabelę
# c.execute("CREATE TABLE users(id SMALLINT, name VARCHAR(30), city VARCHAR(35));")
# query = "INSERT INTO users (id, name, city) VALUES (?, ?, ?);"
# # Wstaw rekordy
# rows = [(5001,'Piotr Nowak',          'Warszawa'),
#         (5002,'Anna Kowalska',        'Kraków'  ),
#         (5003,'Krzysztof Wiśniewski', 'Łódź'    ),
#         (5004,'Maria Wójcik',         'Kraków'  ),
#         (5005,'Andrzej Kowalczyk',    'Wrocław' )]
# c.executemany(query, rows)
# rows = c.execute('SELECT * FROM users;')
# rows = c.fetchall()
# print("Dane użytkowników:")
# for row in rows:
#     print(row)
# print("Zaktualizuj miasto Łódź do Poznania, gdzie id to 5003:") #po ID mamy pewność ze to jest unikalny rekord
# c.execute('UPDATE users SET city = "Poznań" WHERE id = 5003;')
# print("Rekord zaktualizowany pomyślnie.")
# rows = c.execute('SELECT * FROM users;')
# rows = c.fetchall()
# print("Po zaktualizowaniu danych użytkowników:")
# for row in rows:
#     print(row)
# conn.close()
# print("Połączenie SQLite jest zamknięte.")

#TODO Cwiczenie 9 Napisz program w Pythonie, aby usunąć określony (danymi wejściowymi uzytkownika) wiersz z podanej tabeli SQLite i wybrać/wyświetlić w pętli wszystkie wiersze przed i po aktualizacji tej tabeli.
# Przykładowe kolumny tabeli:
# id SMALLINT
# name VARCHAR(30)
# city VARCHAR(35)

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
# Utwórz tabelę
c.execute("CREATE TABLE users(id SMALLINT, name VARCHAR(30), city VARCHAR(35));")
query = "INSERT INTO users (id, name, city) VALUES (?, ?, ?);"
# Wstaw rekordy
rows = [(5001,'Piotr Nowak',          'Warszawa'),
        (5002,'Anna Kowalska',        'Kraków'  ),
        (5003,'Krzysztof Wiśniewski', 'Łódź'    ),
        (5004,'Maria Wójcik',         'Kraków'  ),
        (5005,'Andrzej Kowalczyk',    'Wrocław' )]
c.executemany(query, rows)
rows = c.execute('SELECT * FROM users;')
rows = c.fetchall()
print("Dane użytkowników:")
for row in rows:
    print(row)

delete_id = input("Jakie usunąć ID: ")

print("Zaktualizuj miasto Łódź do Poznania, gdzie id to 5003:") #po ID mamy pewność ze to jest unikalny rekord
c.execute('DELETE from users WHERE id = ?;' ,(delete_id,))

print("Rekord usuniety pomyślnie.")
rows = c.execute('SELECT * FROM users;')
rows = c.fetchall()
print("Po zaktualizowaniu danych użytkowników:")
for row in rows:
    print(row)
conn.close()
print("Połączenie SQLite jest zamknięte.")