print('Hello World')
#TODO; trzeba cos dopisać
print("dowolny tekst")
print('kolejna proba')
#TODO; trzeba cos dopisać
print(4)
x = 2
y = 3

# zmiana intigera na rzeczywistą float()
# zmiana floata na intigera int()
#wprowadzenie liczby intiger
i = 2
print(type(i))
#wprowadzenie liczby float
f = 2.71828e3
print(f)
print(type(f))
#wprowadzenie liczby zespolonej
c = 0.5 + 1j

print(type(c))
#tym danych logicznych - prawda/fałsz
a = 2 > 1
print(a)
#wyświetli wartość True lub False

b = True
#typ zmiennej boolenowe czyli prawda lub fałsz
print(type(a))
b = 2.71828 > 3
#wyp wyrzucający False
print(b)
print(type(b))
#pojedyńczy znak lub ciąg tekstowy
znak = 'A'
print(znak)
#pokazuje ciąg anaków czyli string
print(type(znak))

napis = "Ala ma kota"
print(napis)
print(type(napis))
#indeksy - wyrzucanie fragmentu wyrażenia od startu do wyznaczonego miejsca lod końca lub od startu
znak[0:4]
print(znak)
# napis = "Ala ma kota"
print(napis[0])
print(type(napis[0])) #wyprintowanie typu danych ze srodka printu
print(napis[-1])
print(napis[0:-1])
print(napis[-3:-1])
#ustaliliśmy ciąg wykroju co drugi krok
print(napis[::2])
#dane w zmiennych nie da się podmieniać - bedzie error - można zmienić całą daną nową freścia lub skopiować dane do nowej zmiennej
zmienna = "127"
zmienna = "127"* 127
liczba_calkowita = 2
print(napis + str(liczba_calkowita))
# przy zmienie w drugą strone python też odrówni że mamy do czynienia np z liczbą 1.23

#tym danych krotka - jest to struktura danych definiowana (, , , )

jan = ("Jan", "Kowalski", 33)
janiana = ("Janiana", "Kowalska", (12, 21, 1978), 'K')
print(jan[0])
imie = jan[0]

#lukier składniowy!!!!! ważne
imie, nazwisko, wiek = jan
print (imie, nazwisko, wiek)

#typ lista - różnica jest taka, że każdy element listy można zmienić.

lista = [1, 2, 3, 4, -5, 6, -10]
print(lista)
print(type(lista))
liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]
print(liczby)
imiona = ['Ala', 'Zygmunt', "Alojzy", "Bogusława", (0, 1)]
print(imiona[-1][1]) # print krotki w liście -1 pozycja od tyłu (dojście do krotki) a potem odszukacji piewszego elementu od lewej czyli 0 i 1 jest elementem który zostanie wyrzucony
#wycinanie z listy tak samo dziąła jak wycinanie z krotki
lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
print(lista[1:6])
print(lista[2:6:2]) #wyrzuci od drugiego do szóstego ale co drugi krok
print(lista[::-1]) # wyrzucenie odwróconej iterowalnej listy zaczeliśmy od -1 czyli od końca
print(lista[:]) #wrzucanie dokąłdnie tej samej listy

# modyfikacja list
lista[2:4] = ["pies", "a", "2"]
print(lista) #dodaliśmy i wydłużyliśmy długość listy
print("Witaj")
lista.append("zebra") #append zawsze musi się odnościć do obiektu lista - musimy podać do jakiego obiektu - dodaje na końcu nowy element listy
print(lista)
lista.insert(2,"zebra") #wrzuca dodatkową rzecz po wybranym elemencie w liście w naszym przypadku na 3 miejscu
print(lista)
# notacje .metoda .sort .append (pracujemy na danych obiekcie i wywołujemy coś daną metodą
#lista funkcji znajduje się w build-in metods in python dokumentacja - tak samo jest z wbudowanymi funkcjami
print(lista.pop()) #usuwa ostatni element z listy i printem go wyświetla
print(lista.count("pies"))
# sort
#
#funkcje działające na obiektach sekwencyjnych iterowalnych (int krotka lista)
# len()
# reverse()
#sorted(lista)
#print(lista)
slownik = {"f": [1,2], 'beata':3, "kolejny":3}
print(slownik["kolejny"])

#obiekty typu słownikowego
#wyrzucenie tylko kluczy
print(slownik.keys())

tel = {}  # pusty słownik
print(tel)
tel = {'Maja': 500456, 'Jasio': 123456}
print(tel["Maja"])
#wrzucenie dodatkowej pozycji do słownika na ostatniej pozycji
tel['Ola']= 3004156
print(tel)
#usuwanie elementów slownika
del tel['Maja']
print(tel)
#dict konwertuje z krotki/listy na słownik
tel = dict([('Jan',4139277), ('Kaziemirz', 41267465)])

#zbiór nie może mieć dwóch takich samych elementów - ala zniknie jeden raz
zbior = {"ala", "kot", "ala", 1, 1.23, 2.89}
print(zbior)
#na zbiorach mozna tworzyć działania matematyczne - dodawać, zbrawdzać istnienie, wyrzucac część wspołna
##/
# prawdzenie czy element należy do zbioru:
# zbior: element in zbior
# sprawdzenie czy element nie należy do zbioru:
# zbior: element not in zbior
# odejmowanie od siebie zbiorów:
# c = a - b
# dodawanie do siebie zbiorów:
# c = a | b
# część wspólna zbiorów:
# c = a & b
# część rozłączna zbiorów:
# c = a ^ b
str1 = "FulSlacka"
str2 = round(len(str1)/2)
print(str2)
print(str1[str2-1:str2+1])
##druga opcja tego samego rozwiazania
sampleStr = "Datatypes"
middleIndex = int(len(sampleStr) / 2)
print("Oryginalny ciąg to:", sampleStr)
middleThree = sampleStr[middleIndex-1:middleIndex+2]
print("To są trzy środkowe znaki:", middleThree)
# Oryginalny ciąg to: Datatypes
# To są trzy środkowe znaki: aty

#Łączenie dwa typy ciągów s1 i s2
#oczekiwany wynik FullPythonStack
s1 = "FullStack"
s2 = "Python"
s3 = len(s1)//2
print(s3)
s4 = s1[:s3]
s5 = s1[s3:]
print(s4 + s2 + s5)
#alternatywne rowiązanie bez uzycia dodatkowych zmeinnych
print(s1[:len(s1)//2]+s2+s1[len(s1)//2:])

#Cwiczenie

s1 = "America"
s2 = "Japan"

print(s1[0:1]+s2[0]+s1[:len(s1)//2]+s2[:len(s2)//2]+s1[-1]+s2[-1])

# rozwiazanie
# s1 = "America"
# s2 = "Japan"
# first_char = s1[0] + s2[0]
# middle_char = s1[len(s1) // 2] + s2[len(s2) // 2]
# last_char = s1[-1] + s2[-1]
# res = first_char + middle_char + last_char
# print("Mix String to:", res)

#wyświetlenie znaków od końca do poczatku
str = "Python"
print(str[::-1])

#print("Odwrócony ciąg to:", str1)

tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])
#print("Odwrócony ciąg to:", tuple1)

#wyrzucenie drugiego elementu w liście znajdującej się w krotce na 2 pozycji
tuple1 = ("Pomarańczowy" , [10,20,30],(5,10,15))
print(tuple1[1][1])

#agregacja 2 list do słownika dict konwertuje listy na słownik a zip zmienia
keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
values = [10, 20, 30]
z=dict(zip(keys,values))
print(z)

# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
#
# print(zip(keys, values))
# print(list(zip(keys, values)))
#
# res_dict = dict(zip(keys, values))
# print(res_dict)

#dodanie zbioru do listy i stworzenie nowego zbioru
sample_set = {"Żółty", "Pomarańczowy", "Czarny"}
sample_list = ["Niebieski", "Zielony", "Czerwony"]

#{"Zielony", "Żółty", "Czarny", "Pomarańczowy", "Czerwony", "Niebieski"}
#update nic nie zwraca - wiec nie przypisujemy tego do zmieninej tylko podmieniamy wartość ze zmiennej
sample_set.update(sample_list)
print(sample_set) #wydruk z nowymi wartościami


###
# Typy operatorów
# Arytmetyczne:
# Dodawania: +
# Odejmowania: -
# Mnożenia: *
# Dzielenia: /
# Dzielenia modulo (reszta z dzielenia): %
# Dzielenia całkowitego: //
# Potęgowania: **
###
# Porównania a i b
# a jest równe b: a == b
# a jest różne od b: a != b
# a jest większe od b: a > b
# a jest mniejsze od b: a < b
# a jest większe lub równe b: a >= b
# a jest mniejsze lub równe b: a <= b
# Przypisania
# przypisz do lewej strony wartość z prawej strony: =
# dodaj do lewej strony wartość z prawej strony: += . . .
# Bitowe
# Logiczne: and, or, not


#####TABULATORY########
punkty = 40
if punkty >= 90:
    ocena ='5'
elif punkty >= 75:
    ocena ='4'
elif punkty >= 60:
    ocena ='3'
else:
    ocena= '2'
print(ocena)

### OPERATOR NOT### sprawdza boolenowe wartości
x = False
if not x:
    print('Warunek Spełniony')
else:
    print('Warunek niespoełniony')

### Operator Logiczny AND, OR ###
niepusta_wartosc = 0 or 0.0 or "" or[] or "test" or [123]
print(niepusta_wartosc)
##traeba pamietać że bedzie zwracać wartość z tej tablicy pierszą od lewej która spełnia warunek - nie wartość True/False

kazda_wartosc = 'test' and [123] and []
print(kazda_wartosc)
### wyrzuca piersza wartość która nie spełnia warunek od lewej - tez zwraca WARTOŚć

###lukry składniowe - ma 3 elementy i powoduje skrócenie kodu!!!
# value_if_true if True else value_if_false

wartosc = "warunek spełniony" if True else "warunek niespełniony"

# wartosc = "warunek niespełniony"
# if True: wartosc = "warunek spełniony"

print(wartosc)

nice = True
personality = ("wredny", "miły")[nice]
print("Kot jest", personality)  # Wyjście: Kot jest miły
#Kot jest miły

### PETLA FOR
iterable = [234,123]
for el in iterable:
    print("pracujemy na", iterable.index(el),"elemencie o wartości", el, "z obiektu iterowanego", iterable)

warzywa = ['marchew', 'kalafior', 'kapusta']

for warzywo in warzywa:
    print('warzywo:', warzywo)

### ZAKRES RANGE - niech ta petla wykona sie x razy na okreś;lonych wartościach liczbowych
# Funkcja range() w języku Python wyjaśniona na przykładzie
# Funkcja wbudowana range() generuje liczby całkowite między podaną liczbą całkowitą początkową a liczbą całkowitą zatrzymania, tj. zwraca obiekt zakresu
# Używając pętli for, możemy iterować po sekwencji liczb utworzonych przez funkcję range()
# Zrozummy, jak korzystać z funkcji range() w Pythonie na prostym przykładzie, wraz z wynikiem
print("Przykład range() w pythonie")
print("Uzyskaj liczby z zakresy 0 do 5")
for i in range(6):
   print(i, end=',')

for i in range(10,51,2):
    print(i, end=',')