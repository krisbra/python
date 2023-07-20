# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
#
# simple_function()
# print()
# simple_function()
#
# def my_function():
#     return 3 + 3 # może być wartość krotka, strong wszystko, kończy funkcje
#
#todo ###pamiętajmy żeby wrzucając printa użyć wewnątrz funkcji a nie odnosić sie do zmienych bo na nich nie da się potem robić działań na princie - a na fukcji już tak.
#
# # print(my_function())
# #
#todo######
#
# def add(x, y): ###możemy wpisać y=10 wtedy bedzie defaultowo 10 i tez zadziała)
#     print('x =', x, ', y =', y)
#     return x + y
#
#
# print(add(2, 3))
# # print(add(x=2, y=3)) - tak też można zrobić i mówiąc wprost kolejność wpriowadzania znaków nie ma znaczenia
# # print(add(int(input('x=')), int(input('y=')))) też zadziała i mozeny wprowadzać z ręki rzeczy
#todo ### definiujemy wywołanie i podstawiamy te dane pod wzór
#
#add(2,3)
#
# ##### DOCSTRING
#
# def my_function():
#     """Dokumentacja funkcji"""
#
# help(my_function())
#
#TODO ### rekurencja/rekursja (recursion)
#
# def fibbonaci_numbers(n):
#     '''Zwraca liczby Fibonacciego mniejsze od n'''
#
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         #while len(wynik) <= n:
#         wynik.append(a)
#         a, b = b, a + b
#     return wynik
#
# x = fibbonaci_numbers(10)
# print(x)
# # help(fibbonaci_numbers)
# # print(fibbonaci_numbers.__doc__)
#
#
#
# def fibbonaci_numbers(n):
#     '''Zwraca liczby Fibonacciego mniejsze od n'''
#     wynik = []
#     a, b = 0, 1
# #     while a < n:
#     while len(wynik) <= n: ####robimy pętle dopuki nie uzyskaliśmy n liczb w ciągu - np.
#         wynik.append(a)
#         a, b = b, a + b
#     return wynik
#
# x = fibbonaci_numbers(12+2)
# print(x)
# help(fibbonaci_numbers)
# print(fibbonaci_numbers.__doc__) ###print z atrybutem specjalnym zwraca samą wartość docstringa bez opisu że to docsting
#
# #### Cwiczenia
#todo##funkcja do obliczania długości łańcucha taka jak len
#
#def len2(m):
#     y=0
#     for n in m:
#         y = y+1
#     return y
#
# print(len2(input("Podaj imie ")))
#todo### Napisz funkcję w Pythonie, która zsumuje wszystkie elementy na liście.
#
#nl = [1,2,3,4,5,6,7,8,9]
#
# def suma(lista):
#     suma_p = 0
#     for i  in lista:
#         suma_p = suma_p + i
#     return suma_p
# # print(suma(nl))
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
# # print(sum_list([1, 2, -8]))
#
#todo #### Napisz funkcje w pythonie aby uzyskać największą liczbe z listy
#
#def max_lista(lista):
#     max1 = lista[0]
#     for i in lista[1:]:
#         if i > max1:
#             max1 = i
#     return max1
#
# print(max_lista([0, -5, 654, 100, 100]))
#
# def maks(n):
#     n.sort()
#     return n[-1]
#
# print()
#
#todo #Napisz funkcję w Pythonie, która zlicza liczbę znaków (częstotliwość znaków) w ciągu tekstowym.
# # Przykładowy ciąg tekstowy: google.com
#
# znak = "google.com"
#
# def zlicz (znak):
#     slownik ={}
#     for i in znak:
#         x = slownik.keys() ###funkcja zwraca wszystkie klucze do słownika
#         if i in x:
#             slownik[i] += 1 ### powiekszenie ilości wartości o 1 = czyli dodaje 1 jesli jest już taki znak zliczony
#         else:
#             slownik[i]=1 ####wpisanie wartości 1 pod wartość
#     return slownik
#
# print(zlicz(znak))
#
#todo########Funkcja w Pythonie do zliczania ciągów znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów
#
# lista=['abc', 'xyz', 'a', 'aba', '1221']
# def zlicza(lista):
#     i = 0
#     for elementlisty in lista:
#         if len(elementlisty) >=2 and elementlisty[0]== elementlisty[-1]:
#             i = i + 1
#     return(i)
# print(elementlisty([lista]))
# ??????
########
#todo Funkcja Pythona do pobrania listy, posortowanej w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek
#
# listakrotek=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# #def sort1(listakrotek):
# def sort2(krotka):
#     return krotka[1] ###odwołaliśmy się do drugiego elementu liczyli 0 i 1
# def sort1(listakrotek):
#     listakrotek.sort(key=sort2) ###po key wpisujemy nazwe funkcji
#     return listakrotek
# print(sort1(listakrotek))
#todo ########Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha. Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg
#
# ciag=('PYTHON')
# def lancuch(ciag):
#     if len(ciag) >= 2:
#         return ciag[:2]+ciag[-2:]
#     return '' ###Wyrzuca pusty ciag
# print(lancuch(ciag))
#
#todo ####SILNIA############################
# Napisz program, policzy silnię dla liczby n tj.
# 𝑛!=1⋅2⋅3⋅4...⋅(𝑛−2)⋅(𝑛−1)⋅𝑛
# 𝑛!=(𝑛−1)!⋅𝑛
# 1!=1
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej siebie do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.
#
# def silnia(n):
#     if n == 1:
#         return 1
#     return n * silnia(n-1)
# print(silnia(3))
#
#todo Rekurencyjny ciąg Fibonacciego w Pythonie.

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    #if n<=1: ###połaczenie dwóch poprzednich linijek w jedną
    #   return n
    return fib(n-1) + fib(n-2)
print(fib(5))