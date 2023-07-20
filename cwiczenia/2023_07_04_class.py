# # class NazwaKlasy1:
# #     pass
# # obiekt = NazwaKlasy1() #dwa niezależne od siebie obiekty
# # instancja = NazwaKlasy1()
# # print(type(obiekt))
# # print(type(instancja))
# # print(id(obiekt))
# # print(id(instancja))
# # print(obiekt)
# # print(instancja)
# # class NazwaKlasy:
# #     def nazwa_metody(self, argument1, argument2):
# #         print(argument1)
# #         print(argument2)
# # obiekt = NazwaKlasy()
# # obiekt.nazwa_metody("arg1", "arg2")
# #
# # """Dokumentacja modułu"""
# #
# # class MyClass:
# #     """Dokumentacja klasy"""
# #
# #     def my_method(self):
# #         """Dokumentacja metody"""
# #
# # def my_function():
# #     """Dokumentacja funkcji"""
# #
# # help(MyClass)
# # help(MyClass.my_method)
# # class NazwaKlasy:
# #     atrybut_pierwszy = "Wartość"
# #     atrybut_drugi = 123.0
# #
# # ## jesli sobie stworzymy wewnątrz naszej klasy o nazwie __init__ to jest metoda specjalna uruchamiane automatycznie w pewnych sytuacjach
# # class NazwaKlasy:
# #     def __init__(self, trzeci): #konstruktor to jest to samo co init
# #         self.atrybut_pierwszy = "Wartość" #zeby przechowywać atrybuty wewnątrz obiektów - musi być nazwa obiektu i nazwa atrybutu
# #         self.atrybut_drugi = 123.0
# #         self.atrybut_trzeci = trzeci
# #
# # instancja = NazwaKlasy ("trzeci") #wywołanie klasy - działa na tej samej zasadzie co wywołanie fukncji
# # print(instancja.atrybut_pierwszy)
# # print(instancja.atrybut_drugi)
# # print(instancja.atrybut_trzeci)
# #
# # class MyClass1: #storzenie classy
# #     x = 5
# # p1 = MyClass1() #storzenie obiektu obiektu MyClass
# # print(p1.x) #odwołanie najpierw do obiektu a potem do klasy
# # class Parrot1:
# #     pass
# # obj = Parrot1() ### nie ma konstruktora wiec każdy obiekt bedzie identyczny
# # class Parrot:
# #
# #     # atrybut klasy
# #     species = "papuga" #wspólna wartość dla wszystkich instancji
# #
# #     # atrybut instancji #atrybuty któ®e mogą wyróżnić elementy w klasie
# #     def __init__(self, name, age): #przy wywołaniu itin utworzą się dwa obiekty
# #         self.name = name
# #         self.age = age
# #
# # # utworzenie instancji klasy Parrot
# # blu = Parrot("Blu", 10) #utworzenie pierszego obiektu w konstruktorze
# # woo = Parrot("Woo", 15) #utworzenie drugiego obiektu w konstruktorze
# #
# # # uzyskanie dostępu do atrybutów klasy
# # print("Blu to", blu.__class__.species) #dwa sposoby dobrania się do atrybutu
# # print("Woo to również", woo.species) #dwa sposoby dobrania się do atrybutu
# # # za chwilę wytłumaczymy sobie dokładniej o co chodzi z __class__
# #
# # print(blu.name, "ma", blu.age, "lat")
# # print(woo.name, "ma", woo.age, "lat")
# #
# #
# # class Parrot3:
# #
# #     # atrybuty instancji
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     # metoda instancji
# #     def sing(self, song):
# #         return self.name + " śpiewa " + song
# #
# #     def dance(self):
# #         return self.name + " teraz tańczy"
# #
# # blu = Parrot3("Blu", 10)
# # # wywołanie naszych metod instancji
# # print(blu.sing("'Happy'"))
# # print(blu.dance())
# #
# #
# # class Person:
# #      def __init__(self, name, age): #przy wywołaniu itin utworzą się dwa obiekty
# #         self.name = name
# #         self.age = age
# #      def myfunc(self): #można uzyć self, mysillyobject i abc ####
# #         print("Cześć, mam na imię " + self.name)
# # # utworzenie obiektu klasy
# # p1 = Person("Jan", 36) #utworzenie pierszego obiektu w konstruktorze
# # # uzyskanie dostępu do atrybutów klasy
# # print(p1.name)
# # print(p1.age)
# # p1.myfunc()
# # #można zmieniać atrybuty obiektu - na wyższym poziomie mozemy to zabronić
# # p1.age = 40 #zmieniliśmy atrybut na 40
# # print(p1.age)
# # #można też usuwać atrybuty
# # # del p1.age
# # # print(p1.age) # w takiej sytuacji będzie komunikat jakby nie istaniał obiekt
# # #usuwac mozemy też całe obiekty
# # # del p1 #usuwamy cały obiekt
# # # print(p1)
# # # p1.myfunc()
# #instrukcja pass ## pusta classa i pusta metoda może być utworzona ale musi mieć w środku przynajmniej pass!!
#
# class Person4:
#     pass
#
# class KontoBankowe:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
# jk = KontoBankowe("Jan Kowalski", 1000)
# jk.info()
# jk.wplac(2000)
# jk.wyplac(2500)
#
# #TODO cwiczenie 1
# # Klasa Vehicle bez żadnych zmiennych i metod Utwórz klasę Vehicle bez żadnych zmiennych i metod. Klasa o nazwie MyClass z atrybutem o nazwie x
# # No to jeszcze raz! Utwórz klasę o nazwie MyClass z atrybutem o nazwie x = 5.
# # Teraz użyj klasy o nazwie MyClass do stworzenia obiektu.
# # Utwórz obiekt o nazwie p1 i wydrukuj wartość x.
#
# # class MyClass:
# #     x = 5
# # x1=MyClass()
# # print(p1,x1) ?????
#
# #TODO cwiczenie 2 Klasa (class) dotycząca wyimaginowanego inwentarza odrzutowców jest już dla Was zdefiniowana. Również instancja tej klasy Jets jest stworzona i przypisana do zmiennej first_item. Wydrukuj name z first_item.
#
# # class Jets:
# #     def __init__(self, name, origin):
# #         self.name = name
# #         self.origin = origin
# # first_item = Jets("Boeing 747", "US")
# # a =first_item.name #odwołanie do 1 itemu w Jets
# # print(a)
#
# #TODO Cwiczenie 3 Prosty atrybut (origin) Tym razem wydrukuj origin z first_item.
#
# # class Jets:
# #     def __init__(self, name, origin):
# #         self.name = name
# #         self.origin = origin
# # first_item = Jets("Boeing 747", "US")
# # a = first_item.name
# # b = first_item.origin
# # print(a, b)
#
# #TODO Cwiczenie 4
#
# # class Vehicle: #tworze klase
# #     def __init__(self, max_speed, milage): #tworze atrybut
# #         self.max_speed = max_speed  # do atrybutu przypisuję argument
# #         self.milage = milage
# # first_item = Vehicle("240", "18000") #tworze obiekt
# # a = first_item.max_speed
# # b = first_item.milage
# # print(a,b)
# #
# # #alternatywa rozwiązania
# # x = Vehicle(max_speed=240, milage=1800)
# # print(x.max_speed, x.milage)
#
# #TODO Cwiczenie 5
# # Utwórz klasę Car z dwoma atrybutami instancji:
# # color, który przechowuje nazwę koloru samochodu jako ciąg testowy (str)
# # mileage, który przechowuje liczbę kilometrów przejechanych przez samochód jako liczbę całkowitą (int)
# # Następnie utwórz instancję dwóch obiektów Car - niebieski samochód mający 20 000 kilometrów przebiegu i czerwony samochód mający 30 000 kilometrów przebiegu - i wydrukuj ich kolory oraz przebiegi. Twój wynik powinien wyglądać następująco:
#
# # class Car:
# #     def __init__(self, color, milage): #tworze atrybut
# #         self.color = color  # do atrybutu przypisuję argument
# #         self.milage = milage
# #
# # nc = Car("Niebieski", 20000) #tworze obiekt przed dodanie cudzysłowiów daje pierszy
# # cc = Car("Czerwony", 30000) #tworze obiekt
# #
# # print(nc.color, "samochód ma", nc.milage, "kilometrów przebiegu")
# # print(cc.color, "samochód ma", str(cc.milage), "kilometrów przebiegu") #milage jest int wiec musimy zrobić konwersje na string
#
# #TODO 3 Life Hack
#
#
# # class Car:
# #     def __init__(self, color, milage): #tworze atrybut
# #         self.color = color  # do atrybutu przypisuję argument
# #         self.milage = milage
# # blue_car = Car(color="Niebieski", milage=20_000) #przez wpisanie podkreślnika lepiej bedzie widać tysiące
# # red_car = Car(color="Czerwony", milage=30_000) #tworze obiekt
# #
# # for samochod in (blue_car, red_car): #zdefiniowane funkcji w której odwołujemy się do classy Car
# #     print(f"{samochod.color} samochód ma {samochod.milage:,} kilometrów przebiegu") #przy takim formatowaniu w nawiasie klamrowym jak uzyjemy ":," to uzyje nam separatoru tysięcy
#
# #TODO Cwiczenie 6 Klasa zbudowana na podstawie długości i szerokości oraz metoda, która obliczy pole prostokąta
#
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def pole(self):
#         return self.a * self.b
# x = Rectangle(3, 4)
#
# print("Pole powierzchni a i b wynosi", x.pole())
#
# #TODO Cwiczenie 7 Klasa skonstruowana za pomocą promienia i dwóch metod, które obliczają pole i obwód koła
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def pole(self):
#         return self.r ** 2 * 3.14
#     def obwod(self):
#         return 2 * self.r * 3.14 #można zrobić returna jako pełne działanie i zmienna nie musi cyļ mozna też zaimportować z modułu math prze funcje math.pi liczbe pi dokładna
# x = Circle(8)
# print("Pole wynosi ", x.pole())
# print("Obwór wynosi ", x.obwod())
#
# #TODO Cwiczenie 8 Klasa ma dwie metody; pierwsza metoda przyjmuje ciąg znaków od użytkownika, druga metoda wypisuje ciąg wielkimi literami
#
# class Klasa: #init konstruktor nie jest obowiązkowy!!!!! można wartość wziąć z klawiatury kleinta wiec nie trzeba nic definiować
#     def get_string(self):
#         self.lista = input("Podaj ciąg znaków: ")
#     def print_string(self):
#         print(self.lista.upper())
#
# p1 = Klasa()
# p1.get_string() #komunikacja między tymi dwoma metadami działa niezaleznie
# p1.print_string() #komunikacja między tymi dwoma metadami działa niezaleznie