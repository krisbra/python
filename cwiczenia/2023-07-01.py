# #TODO "Funkcje Anonimowe (LAMBDA)"
# lambda arg1, arg2: arg1 ** arg2
# gdzie
# lambda - key word
# arg1, agr2 - argumenty
# : <- jako return
# arg1 ** arg2 - co ma zrobić z tymi elementami
#
# c*c = a*a + b*b
# ** potenga
# 1/n
# #TODO przykład 1
# def c_sum(x, y):
#     return x + y
# l_sum = lambda x, y: x + y
# print(c_sum(4,4))
# print(l_sum(4,4))
# #TODO przykład 2
# z = lambda a: a
# z(2)
#
# #TODO przykład 3
# #Napisz program w Pythonie, aby utworzyć funkcję lambda, która dodaje 15 do podanej liczby przekazanej jako argument
# ad15 = lambda a: a+15
# print(ad15(5))

#TODO przykład 4
# #Lista krotek

# subject_marks = [('jezyk anglieski', 88),
#                  ('Nauka', 90),
#                  ('Matematyka', 97),
#                  ('Nauki społeczne', 82)]
# print("Oryginalna lista krotek: ")
# print(subject_marks)
# subject_marks.sort(key=lambda x: -x[1]) # jeśli chcemy w odwróconej kolejności to dajemy -1
# print("\n Sortowana lista krotek: ")
# print(subject_marks)

#TODO przyklad 5 # dla słownika musimy używać metody sorted!!! Sort nie zadziała

# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
#
# print("Oryginalna lista slownika: ")
# print(models)
# #sorted_models.sort(key=lambda x: x[0]) ### ten zapis nie zadziała
# print("słownik po zmianach: ")
# #print(sorted_models)
# sorted_models = sorted(models, key = lambda x: x['kolor'])
# print(sorted_models)

#TODO Napisz program w Pythonie, aby sprawdzić, czy dany ciąg zaczyna się od znaku 'P', używając lambda
# Podpowiedź: skorzystaj z funkcji (metody) startswith()
#
# starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('python'))
# #wynik tego wrzuca nam true lub false jeśli pierwsza litera bedzie odpowiednia
#
# #TODO przykład wywołujący rok, miesiąc , dzień i godzinę
#
# import datetime
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))
# now.year

#TODO przykład Napisz program w Pythonie, aby sprawdzić, czy dany ciąg jest liczbą, czy nie, używając lambda
# Podpowiedź: przydatna metoda to
# string.replace(oldvalue, newvalue, count)
# Składnia parametrów:
# oldvalue – Wymagany; ciąg do wyszukania
# newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
# count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić; domyślnie są to wszystkie wystąpienia
#
# is_num = lambda q: q.replace('.', '', 1).isdigit()
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))
# print("\nWydrukuj liczby kontrolne:")
# is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)
# print(is_num1('-16.4'))
# print(is_num1('-24587.11'))
# is_alpha_numeric = lambda q: q.replace('.', '', 1).isalnum()
# print(is_alpha_numeric("Mikolaj2023"))

# #TODO filtrowanie, mapowanie, redukowanie
#
# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3
# ]
# wynik = list(filter(lambda x: x>=40.0, temperatury))
# wynik_sort = sorted(wynik)
# print(wynik_sort)

#TODO Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# wynik_parz = list(filter(lambda x: x % 2 == 0, nums))
# print(wynik_parz)
# wynik_nparz = list(filter(lambda x: x % 2 != 0, nums))
# print(wynik_nparz)

#TODO Napisz program w Pythonie, aby znaleźć przecięcie dwóch podanych tablic za pomocą lambda i filter
# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10] #lista
# array_nums2 = [1, 2, 4, 8, 9]

# array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array_nums2 = [1, 2, 4, 8, 9]
# print("Oryginalne tablice:")
# print(array_nums1)
# print(array_nums2)
# result = list(filter(lambda x: x in array_nums1, array_nums2))
# print("\nPrzecięcie wspomnianych tablic: ", result)

#TODO Napisz program w Pythonie, aby policzyć parzyste i nieparzyste liczby w danej tablicy liczb całkowitych, używając lambda i filter
# array_nums = [1, 2, 3, 5, 7, 8, 9, 10]

# array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
# print("Oryginalna tablica:")
# print(array_nums)
# odd_list = list(filter(lambda x: (x % 2 != 0), array_nums))
# print(f'Nieparzysta lista: \n {odd_list}')
# odd_ctr = len(list(filter(lambda x: (x % 2 != 0), array_nums)))
# even_list = list(filter(lambda x: (x % 2 == 0), array_nums))
# print(f'Parzysta lista: \n {even_list}')
# even_ctr = len(list(filter(lambda x: (x % 2 == 0), array_nums)))
# print("\nLiczba liczb parzystych w powyższej tablicy: ", even_ctr)
# print("\nLiczba liczb nieparzystych w powyższej tablicy: ", odd_ctr)

#TODO Napisz program w Pythonie, aby znaleźć wartości o długości sześć na podanej liście za pomocą funkcji lambda i filter
#weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
#
# weekdays = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
# len_6 = list(filter(lambda x: len(x)==6,weekdays))
# # print(len_6)
# print(len(len_6))

#TODO Napisz program w Pythonie, aby znaleźć liczby podzielne przez dziewiętnaście lub trzynaście z listy liczb za pomocą lambda i filter
# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#
# nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# dziel = list(filter(lambda x: x % 13 == 0 or x % 19 == 0, nums))
# print(dziel)

#TODO Napisz program w Pythonie, aby znaleźć palindromy na podanej liście ciągów za pomocą lambda i filter
# Palindrom – wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# Przykładem palindromu jest: „kobyła ma mały bok”
# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
#
# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# palindrom = list(filter(lambda x: x[::] == x[::-1], texts)) #nie musimy użyć[::] moze być samo x
# print(palindrom)
#
#TODO alternatywne rozwiązanie

# texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# print("Oryginalna lista ciągów:")
# print(texts)
# result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
# print("\nLista palindromów:")
# print(result)

#TODO przykład Napisz program w Pythonie, który zsumuje długość nazw z danej listy nazw po usunięciu nazw zaczynających się od małej litery
# Użyj funkcji
# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
#
# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
# sumowanie = list(filter( lambda x: x[0].islower(), sample_names))
# print("\nLista slow z malej litery: ")
# print(sumowanie)
# print("\nsuma znaków: ")
# print(len(''.join(sumowanie))) #łącznie bez dodawania żadnego dodatkowego znaku
# print('tu_można_wstawić_dowolny_obiekt_string'.join(sumowanie))

#TODO przykład srednia z liczb oraz zaokrąglenie

# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3]
#
# from statistics import mean
# sr_temp = mean(temperatury)
# print(sr_temp)
# odch = round(temperatury[0] - sr_temp,2)
# print(odch)

#TODO map Napisz program w Pythonie podnoszący do kwadratu i sześcianu każdą liczbę z podanej listy liczb całkowitych, używając lambda i map
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Oryginalna lista liczb całkowitych:")
# print(nums)
# print("\nKwadrat każdej liczby z listy:")
# square_nums = list(map(lambda x: x ** 2, nums)) #dodajemy map który rpzechodzi przez każdy element listy
# print(square_nums)
# print("\nSześcian każdej liczby z listy:")
# cube_nums = list(map(lambda x: x ** 3, nums))
# print(cube_nums)

#TODO Napisz program w Pythonie, aby dodać dwie podane listy za pomocą map i lambda

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# print("Oryginalna lista:")
# print(nums1)
# print(nums2)
# suma = map(lambda x, y: x + y, nums1, nums2)
# print("\nWynik: po dodaniu dwóch list")
# print(list(suma))
# print("\nWynik: po mnożeniu dwóch list")
# iloczyn = list(map(lambda x, y: x*y, nums1,nums2)) #map na listach zwraca na pewno list
# # iloczyn = map(lambda x, y: x*y, nums1,nums2)
# print(list(iloczyn))

#TODO Napisz program w Pythonie, który za pomocą funkcji lambda mnoży każdą liczbę z podanej listy przez określoną liczbę
# Wydrukuj wynik
# nums = [2, 4, 6, 9, 11]
# n = 2

# nums = [2, 4, 6, 9, 11]
# n = 2
# print("Oryginalna lista: ", nums)
# print("Podana liczba: ", n)
# filtered_numbers = list(map(lambda number: number*n, nums)) #tu musi być list be jeden obiekt jest2 i nie jest to lista
# print("Wynik:")
# print(' '.join(map(str, filtered_numbers)))

#TODO REDUKOWANIE

# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a + b, nums))
# ## to samo można uzyskać w stosując
# # sum(nums)
# # print(sum(nums))

#TODO suma liczb w ciągu fibonaciego

from functools import reduce

#TODO Napisz program w Pythonie do tworzenia ciągu Fibonacciego aż do n za pomocą lambda i reduce
# Podpowiedzi:
# Da się to zrobić w zasadzie w jednej linijce!
# Przypomnij sobie, co robiła zmienna _
#
# from functools import reduce
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
# print("Ciąg Fibonacciego do 2:")
# print(fib_series(0))
# print("Ciąg Fibonacciego do 5:")
# print(fib_series(5))

#TODO LIST COMPREHENSION upraszaczmy składnie - co wykonać - dlaczego - i w jakim zakresie
# nowa_lista = [funkcja(element) for element in lista if warunek(element)]
#
# kwadraty = [el**2 for el in range(1, 102) if el % 2 != 0]
# print(kwadraty)
#range(1,102) -> <1, 102)

#TODO Napisz program w Pythonie, który usuwa liczby dodatnie z podanej listy liczb
# Zsumuj liczby ujemne i wydrukuj wartość bezwzględną za pomocą tworzenia listy – ang. list comprehension
# Wydrukuj wynik

# nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# print("Oryginalna lista: ", nums)
# print("Wynik:")
# #Step 1: wygenerowanie listy liczb ujemnych
# ujemne = [i for i in nums if i < 0]
# print(ujemne)
# print(sum(ujemne))
# print(abs(sum(ujemne)))
# #list comprehension
# print(abs(sum([i for i in nums if i < 0])))
# #standardowe podejście iteracyjne
# result = []
# for num in nums:
#     if num < 0:
#         result.append(num)
# print(abs(sum(result)))

#TODO Napisz program w Pythonie, aby zmienić kolejność liczb dodatnich i ujemnych w danej tablicy (najpierw wszystkie ujemne, potem wszystkie dodatnie) za pomocą tworzenia listy – ang. list comprehension

# array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
# print("Oryginalna tablica:")
# print(array_nums)
# print(f'Wygenerowana lista liczb ujemnych: {[x for x in array_nums if x < 0]}')
# print(f'Wygenerowana lista liczb dodatnich: {[x for x in array_nums if x >= 0]}')
# result = [x for x in array_nums if x < 0] + [x for x in array_nums if x >= 0]
# print("\nZmiana kolejności liczb dodatnich i ujemnych wspomnianej tablicy:")
# print(result)

#TODO Napisz program w Pythonie, aby:
# Znaleźć liczby z podanego ciągu. Zapisać je na liście. Wyświetlić liczby w posortowanej formie
# Użyj funkcji tworzenia listy – ang. list comprehension, aby rozwiązać problem
#
# str1 = "euro 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
# print("Oryginalny ciąg: ", str1)
# str_num = [i for i in str1.split(' ')]
# print("Oryginalna lista: ", str_num)
# numbers = sorted([int(x) for x in str_num if x.isdigit()])
# print('Liczby w posortowanej formie:')
# for i in numbers:
#     print(i, end=' ')
# print(numbers)

#TODO Napisz list comprehension, który stworzy listę zawierającą kwadraty liczb od 1 do 10.

# lista = [ x ** 2 for x in range(1,11)] # x **2 warunek który jest na poczatku jest modyfikowalny w zależności od oczekiwanego efektu
# print(lista)

#TODO Napisz list comprehension, który stworzy listę zawierającą podwojone wartości liczb parzystych od 1 do 20.

# x = [i*2 for i in range(1,21) if i%2 == 0]
# print(x)

#TODO Napisz list comprehension, który stworzy listę zawierającą długości słów w podanym zdaniu: "Python jest niesamowity".

# string = 'Python jest niesamowity'
# string.split()
# x = [i for i in string.split()] #stworzyliśmy listę słów i wrzuciliśmy ją w liste
# print(x)
# x = [len(i) for i in string.split()] # po stworzeniu listy zlicza ilość znaków w liście
# print(x)

#TODO Napisz list comprehension, który stworzy listę zawierającą tylko liczby nieparzyste z podanej listy: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = [i for i in lst if i%2!=0]
# print(x)


#TODO STRINGI SĄ NIEZMIENNE
# 4 = sting
# hello = float

#TODO przykłady Napisz funkcję anonimową obliczającą kwadrat danej wartości
# Czy potrafisz wytłumaczyć czym się to różni od użycia funkcji
# pow(a, b)
# lub operatora
# a ** b
#
# # srednia = lambda x,y: (x+y)/2
# print(srednia(2,3))

#TODO Napisz funkcję anonimową sprawdzającą czy dana wartość jest większa (lub mniejsza) od pewnej wartości
# Taka funkcja anonimowa powinna zwracać wartość logiczną

# funkcja = lambda x,y: x<=y
# print(funkcja(4,5))
#
# lambda x,y: True if x<=y else False
# print(funkcja(9,8))

#TODO Stwórz listę temperatur przy pomocy list comprehension i modułu random
# Znajdź wszystkie wartości mniejsze od 36.6
#
# import random
# x = [round(random.uniform(35,37),2) for i in range(1,20)]
# lst = list(filter(lambda x: x<36.6,x))
# print(lst)

#TODO Odfiltruj wszystkie wartości, które są.
# Stwórz listę przetrzymującą wzrost 50 osób, korzystając z list comprehension i modułu random
# Odfiltruj wszystkie wartości, które są:
# Mniejsze bądź równe 120, lub
# Większe bądź równe 205
#
# import random
# lst = [random.randint (100,250) for i in range(50)]
# print(lst)
# lst2 = list(filter(lambda x: x < 120 or x > 205, lst))
# print(lst2)

#TODO Oblicz dla każdej liczby w zbiorze temperatur kwadrat:
# Różnicy tej liczby, i
# Średniej arytmetycznej całego zbioru
#
# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3]
# from statistics import mean
# sredniaListy = mean(temperatury)
# print(sredniaListy)
# kwadratyRoznic = list(map( lambda x: (x - sredniaListy)**2,temperatury))
# print(kwadratyRoznic)

#TODO Zadanie 7 Mając obliczone wartości odchyleń temperatur od średniej temperatury, oblicz wariancję tych wartości
# Wariancja:
# Klasyczna miara zmienności
# Intuicyjnie utożsamiana ze zróżnicowaniem zbiorowości
# Jest średnią arytmetyczną kwadratów odchyleń (różnic):
# Poszczególnych wartości cechy, od
# Wartości oczekiwanej
# https://www.matemaks.pl/wariancja.html
# Nie zapomnij o podzieleniu przez ilość elementów w zbiorze!

# from statistics import mean
# import random
# temp = [round(random.uniform(35, 42),2) for i in range(20)]
# std_dev =mean(list(map(lambda x: (x - mean(temp))**2,temp)))
# print(std_dev)

#TODO Napisz pogram, który policzy kwadraty liczb z zakresu [1,10000], które podzielne są przez:
# 5, lub 9 Następnie sprawdź, które z uzyskanych liczb są podzielne:
# Zarówno przez 5 Jak i przez 9 ###LIST COMPREHENSION

lista = [i**2 for i in range(1,10000) if i % 5 == 0 or i % 9 == 0] #list comprehention liczby podzielne przez 5 lub 9 podniesione do kwadratu
print('Lista liczb podzielnych przez 5 lub 9 to: \n',lista)
lista2 = [ x for x in lista if x % 5 == 0 and x % 9 == 0]
print('Lista liczb podzielnych przez 5 oraz 9 to: \n',lista2)
#to samo w formie klasycznej petli - tylko w formie pętli for
lista11 = []
for i in range(1,10000):
    if i % 5 == 0 or i % 9 == 0:
        lista11.append(i**2)
print(lista11)
assert lista == lista11

#TODO Wygeneruj listę za pomocą list comprehention, która będzie miała

