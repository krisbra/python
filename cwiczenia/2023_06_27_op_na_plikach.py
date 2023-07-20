### https://docs.python.org/3/library/functions.html#open
##TODO PRACA NA PLIKACH
### open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)¶
# f = open('write_file_name', 'w') <-- nazwa obiektu jako string - oznacza to że pod zmienną f będzie plik otwarty na którym mozemy robić działania
# f = open('append_file_name', 'a')
# f = open('read_file_name', 'r') ###jest jeszcze x, b, t, +
#
# f.read() ### przeczyta całą zawartość pliku
#
# f.readline() ###<przeczyta nam jedną linię tekstu
#
# f.readlines() ###<przeczyta nam określone linie tekstu

#TODO Ćwiczenie
# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.
#
# # f.write("tekst") ### jest to zapis do pliku
# f = open('plik.txt', 'a') #argument w powoduje write nadpisanie pliku; agrument a powiduje dodanie do pliku
# try:
#     f.write("\n" + 'nowa linia \n') #zapis z uzyciem nowej linii
# except:
#     print("Problem z zapisem do pliku")

##TODO zapis do pliku - trzeba pamietać o typie danych value jest int a domyślnie write działa na stringach
# f.write('Witaj\n')
#
# value = 42
# f.write(value)
#
# >>>Traceback (most recent call last):
# >>> File "<stdin>", line 1, in <module>
# >>>TypeError: must be str, not int
# s = str(value)  ### musimy zamkąć plik jako string wiec dlatego określamy value tego pliku inaczej się nie zapisze
# f.write(s)
# f.close()

#TODO Metoda pliku Pythona
# fileObject.seek(offset[, whence])
# ustawia aktualną pozycję pliku na przesunięcie
# Argument whence jest opcjonalny:
# 0 – oznacza bezwzględne pozycjonowanie pliku (taką przyjmuje wartość domyślną)
# 1 – oznacza szukanie względem bieżącej pozycji
# 2 – oznacza szukanie względem końca pliku
# f.seek(0) # na początek
# f.seek(0, 2) # na koniec
#
# # Otwórz plik
# fo = open("plik1.txt", "r", encoding="UTF-8") #dodanie encoding daje pewność odczytu polskich znaków
# print("Nazwa pliku: ", fo.name)
# line = fo.readline() ###trzeba pamietać o tym że przenosi nas do tego miejsca w tekście - czyli kolejne wywołanie bez określenia miejsca zacznie od tego miejsca
# print("Czytaj linię: >" + line + "<")
# pos = fo.tell() # odczytanie fo.tell pokazuje aktuaną pozycję
# print("Aktualna pozycja: " + str(pos))
# # Ponownie ustaw wskaźnik na początek
# #fo.seek(0, 0)  # fo.seek(0)
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Zamknij otwarty plik
# fo.close()

#TODO "MODUŁY"
#
# import <nazwa-modułu>
# import <nazwa-moduły as <alias>
# ex.
#
# #przykład no 1
#
# import math
# x=4
# math.sqrt(x) #można to wywołać bezpośrednio w print
# print(math.sqrt(x))
# #przykład 2
#
# import math as m
# import pandas ### cały szary to znaczy że moduł jest nie zainstlowany
# x=100
# m.sqrt(x) #można to wywołać bezpośrednio w print
# print(m.sqrt(x))
# import pandas
## dodajemy plik konfiguracyjny requirements.txt !!!!!
## komendom from możemy odnieść się do konkretnej jednej funkcji
# from math_op import return_sqrt ###importowanie z konkretnej funkcji z modułu
# # biblioteka os
# import os
# print(dir(os.system))
#print(os.system("pip install pandas"))
# print(os.system("pip install --upgrade pip"))
#os.mkdir('00_abcd') #komenda tworzaca katalog w miejscu w którym jesteś
#cd ..  wyjście kat wyżej
#ls lista plików
# #
# os.system('ls')
# from time import sleep
# sleep(2)
# print("Dzień dobry")
# from time import * ## gdzieki gwiazdce też nie musimy poźniej odnosić się do math_op tylko od razu do return
#
# if __name__ == "__main__": ### "__" to jest wywołanie underami

# import glob
# print(glob.glob('*')) #wyświetla wszystkie pliki w katalogu w któ®yms ię znajdujemy
#
# import os.path
# print(os.path.exists('plik.txt')) ##zwraca True jeśli jest plik lub False jesli nie ma
#
# import shutil
#
# shutil.copyfile('plik.txt', 'dst=cd.. 00_abcd/text2.txt')
#

#shutil.rmtree('00_abcd') #usunięcie katalogu


# # 1) bez użycia instrukcji with
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()
# # 2) bez użycia instrukcji with
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()
# # 3) używanie instrukcji with
# with open('file_path', 'w') as file:
#     file.write('hello world !')
#     pass

#TODO przykłąd 1
# Napisz program w Pythonie, aby odczytać i wyświetlić cały plik tekstowy.

# txt = open('plik1.txt')
# # print(txt.read())
# # txt.close()
#
# with open('plik1.txt', 'r', encoding='UTF-8') as file:
#     content_list = file.readlines()
#     print(content_list)

#TODO przykład 2
# Napisz program w Pythonie, który odczyta wszystkie wiersze pliku tekstowego, zapisz go w zmiennej.

# with open('plik1.txt', 'r', encoding='UTF-8') as file:
#     content = file.read()
# print(content)

#TODO przykład 3
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu, zapisz go w tablicy `content_array`.
# `content_array` to lista zawierająca przeczytane wiersze.

# content_aray = []
# with open('plik1.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         content_aray.append(line)
# print(content_aray)

#TODO przykład 4
# Napisz program w Pythonie, który odczyta pierwsze n wierszy pliku. Użyj funkcji itertools.islice
#dzieki n możemy przywołać wprowadzoną przez uzytkownika liczbę linii która musi zostać wyświetlona
#
# import itertools
# n = int(input('Podaj liczbę: '))
# with open('plik1.txt', 'r', encoding='UTF-8') as file:
#     for line in itertools.islice(file, n):
#         print(line)

#TODO przykład 5
# Napisz program w Pythonie, który znajdzie najdłuższe słowa w pliku tekstowym.

# def naj_slowo(plik):
#     listslowa = []
#     with open(plik) as file:
#         slowa = file.read().split()
#         maxz = len(max(slowa, key=len))
#         print(maxz)
#         for word in slowa:
#             if len(word) == maxz:
#                 listslowa.append(word)
#     return listslowa
#
#
# print(naj_slowo('plik1.txt'))

#TODO Przykład 6
# Napisz program w Pythonie, który zlicza liczbę wierszy w pliku tekstowym.

# def suma_wierszy(plik):
#     with open(plik) as file:
#         suma_lista = file.readlines()
#         print(suma_lista)
#         len(suma_lista)
#         print(len(suma_lista))
# print(suma_wierszy('plik1.txt'))

#TODO Przykład 7 Odczytanie ilości słów w pliku tektowym

# with open('plik1.txt') as file:
#     lista = file.read().split()
#     print(len(lista))

#TODO Przykład 8 Napisz program w Pythonie, który zapisze listę do pliku.

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('plik2.txt', 'w') as file:
    for item in colors:
        file.write(item + '\n') #wpisanie wszystkich elementów z listy każda od nowej linijki
