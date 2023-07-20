### Exception Hierarhy
### library https://docs.python.org/3.11/library/exceptions.html#exception-hierarchy
### Obsługa wyjątków try -> except -dodatkowo może być -> else/finally
# try: - run this code
# except: execute this code when there is an exception
# else no exceptions Run tis code
# finally: always tun this code
#
# #przykład
# try:
#     <linie kodu>
# except exception as err:
#     <obsługa wyjątku>
# else:
# #     print ('wszystko ok')
# # finally:
# #     print('cos co na się zadziać na końcu')
# #
# # Wstawiamy gdziekolwiek w kodzie jeśli chcemy podnieść raise - stawiamy jesli chcemy żeby program się wyłożył zgłownie po if
# #
# # ## https://peps.python.org/pep-0000/ tu jest informacja jak pisać kod ładnie PEP - jest to zbiór zasad.
#
# #todo pierwszy przykład
# import sys
# try:
#     f = open("plik.txt", "r") #otwieranie pliku - atrybut "r" oznacza czytanie
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu:", err)
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:  # PEP 8: E722 nie używaj pustego 'except'
#     print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#     raise
# finally:
#     file.close() #komenda zamkniecia pliku - jeśli
#
# print('Dalsza część kodu')
#
# #TODO przykład 2
#
# try:
#     print("Dzień dobry")
# except:
#     print("Coś poszło nie tak")
# else:
#     print('Wszystko ok;)')
# finally:
#     print("Klauzula try except jest zakończona")
#
# #TODO przykad 3
# # Blok try zgłosi błąd podczas próby zapisu do pliku tylko do odczytu::
#
# try:
#     file = open("demofile.txt", "r")
#     try:
#         file.write("Lorum Ipsum")
#     except:
#         print("Coś poszło nie tak podczas ZAPISYWANIA do pliku")
#     finally:
#         file.close()
# except:
#     print("Coś poszło nie tak podczas OTWIERANIA pliku")
# # Coś poszło nie tak podczas ZAPISYWANIA do pliku
#
# #todo obsługa raise Wywołaj błąd i zatrzymaj program, jeśli x jest mniejsze niż 0
# def dowolnaFunkcja(x):
#     if x < 0:
#         raise Exception("Przepraszamy, brak liczb poniżej zera")
#     print(x)
# dowolnaFunkcja(-1);
# def dowolnaFunkcja(x):
#     if x < 0:
#         raise Exception("Przepraszamy, brak liczb poniżej zera")
#     print(x)
#
# dowolnaFunkcja(-1);
#
# #TODO kolejny przykład raise
# # Przykład 2 - Podnieś TypeError, jeśli x nie jest liczbą całkowitą (int)
# # In [42]:
#
# x = 1
# x = "dzień dobry"
#
# if not type(x) is int:
#     raise TypeError("Dozwolone są tylko liczby całkowite")

# #TODO cwiczenie
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.
# def Walidacjaliczb():
#     print("Podaj dwie liczby.")
#     try:
#         x = int(input('liczba1: '))
#         y = int(input('liczba2: '))
#         print(x+y)
#     except Exception as err1:
#         print:("Błąd typu danych. Wprowadź liczbę", err1)
#         Walidacjaliczb()
#
# Walidacjaliczb()
# ???????
#
# #TODO dzielenie przez 0
# a = 5
# b = 0
# try:
#     result = a / b
# except ZeroDivisionError:
#     result = "Nie możesz podzielić przez 0"
#
# print(result)
#przykład alternatywny
# def Dzielenie(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         result="Nie możesz podzielić przez 0"
#     return result
# print(Dzielenie(5,2))

#TODO kolejny przykład
# Napisz dowolny kod.
# Wychwyć w nim wyjątek, ale nic nie rób.
#
# lista = [1, 2, 3]
# print(lista)
# print(type(lista))
# try:
#     print(lista[3])
# except IndexError: #w naszym przypadku odwołaliśmy się do konkretnego błędu IntaxError
#     pass #też to będzie działać - czyli kod się wykona mimo odwołania do 4 elementu z listy

#TODO Spróbuj dodać int do str, a wynik przypisać do msg.
# Umieść:
# msg = "Nie możesz dodać int do str"
# aby program uniknął błędu BaseException.
# Możesz użyć wyjątku Exception, chociaż zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.

# x = "Python"
# y = 5
# try:
#     print(x+y)
# except TypeError:
#     print("nie da się dodać ", x, y)

#TODO Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines())).
# Na koniec zamknij ten plik (podpowiedź: f.close()).
#
# arg="plik.txt"
# try:
#     f = open(arg, "r")
# except:
#     print("Problem z otwarciem pliku")
# else:
#     print(len(f.readlines()))
#     f.close()
# #alternatywa prowadzącego
#
# arg = "nieistniejacy_plik"
# try:
#     f = open(arg, "r")
# except IOError: #IOError taka biblioteka
#     print(f"Nie mogę otworzyć pliku: '{arg}'")
# else:
#     print(f"Plik: '{arg}' ma {len(f.readlines())} wierszy")
#     f.close()

