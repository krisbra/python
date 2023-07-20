# class KontoBankowe:
#      def __init__ (self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
#
# class KontoDebetowe(KontoBankowe):
#     pass
#
#TODO Przy dziedziczeniu nadpisujemy konkretne linie kodu Konata BAnkowego poprzez nadanie innych elementów w KoncieDebetowym
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan = 0, minit = 0): ##sposób w jaki dziedziczymy
#         KontoBankowe.__init__(self,nazwa,stan) ##sposób w jaki korzystamy
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan kont  po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             KontoBankowe.wyplac(self, ilosc)
# account = KontoDebetowe("Jan Nowak", 0, 1000)
# account.info()
# nazwa: Jan Nowak
# stan: 0
# account.wplac(500)
#
# print(account)
#
# account.info()
# nazwa: Jan Nowak
# stan: 500
# account.wyplac(1000)
# account.info()
# nazwa: Jan Nowak
# stan: -500
#
# account.wyplac(1000)
# Brak srodkow na koncie
#
# account.info()
# nazwa: Jan Nowak
# stan: -500
#
# ##TODO OPCJA SUPER Aby wywołać metodę klasy bazowej, zamiast wpisywać długie wyrażenie NazwaKlasyBazowej można użyć metody super() zwracającej klasę rodzica. Jest to szczególnie przydatne jeśli zmienimy nazwę klasy bazowej, nie trzeba będzie wtedy wprowadzać zmian w klasach pochodnych. Przykład z kontem bankowym:
#
# # bylo:
#     def __init__(self, nazwa, stan=0, limit=0):
#         KontoBankowe.__init__(self, nazwa, stan)
#         self.limit = limit
# # jest:
#     def __init__(self, nazwa, stan=0, limit=0):
#         super().__init__(nazwa, stan)
#         self.limit = limit
#
# class KontoDebetowe(KontoBankowe):
#     def __init__(self, nazwa, stan=0, limit=0):
#         super().__init__(nazwa, stan)
#         self.limit = limit
#
#     def wyplac(self, ilosc):
#         """Jeżeli stan konta po operacji przekroczyłby limit, przerwij."""
#         if (self.stan - ilosc) < (-self.limit):
#             print("Brak srodkow na koncie")
#         else:
#             super().wyplac(ilosc)
# ##TODO DZIEDZICZENIE KLASY Wielokrotne dziedziczenie
# # Trochę jak w prawdziwym życiu w rodzinie, klasa pochodna może mieć więcej niż jednego przodka i od każdego przodka zbierać atrybuty i metody.
#
# #TODO wykorzystanie klasy
# A.__init__()
#
# #TODO __doc__
# #__doc__ dokumentacja w doc stringach nie jest dziedziczona __doc__ - ciąg dokumentacji lub None, jeśli nie jest dostępny; nie dziedziczone przez podklasy.
#
#
# print(A.__doc__)
# print(B.__doc__)
# print(Pochodna.__doc__)
#
# d = Pochodna()
# print(d.a)
# A
# print(d.b)
# B
# d.fa()
# a: A
# d.fb()
# b: B
#
# ## Jak widać klasa Pochodna zawiera pola i metody od każdego z rodziców.
#
# import math
# class Figura:
#     def obwod(self): #L
#         raise NotImplementedError
#     def pole(self): #S/P
#         raise NotImplementedError
#
# # f=Figura()
# # f.obwod()
# print(math.pi)
# class Figura:
#     def obwod(self):  # L
#         """Obliczanie obwodu."""
#         raise NotImplementedError
#     def pole(self):  # S/P
#         """Obliczanie pola powierzchni."""
#         raise NotImplementedError
# class Kolo(Figura):
#     def __init__(self,r):
#         self.r = r
#     def obwod(self):
#         return math.pi * 2 * self.r
#     def pole(self):
#         return math.pi * self.r**2
# x = Kolo(10) ##dzieki temu w obiekcie 10 zostanie przypisane do r
# print(x.obwod()) #nazwa obiektu.metoda
# print(x.pole())
# print(" Obwód koła o promieniu ", x.obwod(), " wynosi ", x.obwod())
# print(x.obwod())
#
# class Trojkat(Figura):
#     def __init__(self,a):
#         self.a = a
#     def obwod(self):
#         return 3 * self.a
#     def pole(self):
#         return self.a**2 * math.sqrt(3) / 4
#
#     # def __rep__ ### odwołanie się do obiektu wewnątrz zmiennej - doczytać! https://www.programiz.com/python-programming/methods/built-in/repr
# y = Trojkat(5)
#
# print(" Obwód trojkata o boku ", y, " wynosi ", y.obwod()) #tak nie da się wywołać wartości wewnątrz Y widzimy cały obiekt
# print(" Pole trojkata o boku ", y, " wynosi ", y.pole())
#
#
# class Prostokat(Figura):
#     def __init__(self,a , b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return 2 * (self.a + self.b)
#     def pole(self):
#         return self.a * self.b
#
# z = Prostokat(10,20)
#
# print(" Obwód Prostokata wynosi ", z.obwod())
# print(" Pole Prostokata o bokach wynosi ", z.pole())
#
# class Kwadrat(Prostokat):
#     def __init__(self,a):
#         # self.a = a #pierwsze rozwiazanie
#         # self.b = a
#
#         Prostokat.__init__(self,a,a) #drugie rozwiazanie
#
#         # super().__init__(a,a) #dzieki temu nadpisujemy argumenty jest to trzecie rozwiazanie
# z = Kwadrat(10)
#
# print(" Obwód Kwadratu wynosi ", z.obwod())
# print(" Pole Kwadratu o bokach wynosi ", z.pole())
#
# #TODO Cwiczenie 2 Utwórz obiekt klasy Bus, która dziedziczy wszystkie zmienne i metody klasy Vehicle i wyświetli je.
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# x = Bus("Szkolene Volvo", 180, 120)
#
# print("Nazwa pojazdu: ", x.name, "Prędkość: ", x.max_speed)

#TODO Cwiczenie 3
# Zmienne utworzone w .__init__() nazywane są zmiennymi instancji. Wartoś  zmiennej instancji jest specyficzna dla konkretnego wystąpienia klasy. Na przykład w rozwiązaniu obiekty wszystkie obiekty Vehicle mają name i max_speed, ale wartości zmiennych name i max_speed będą się różnić w zależności od instancji Vehicle.
# Z drugiej strony atrybuty klasy to atrybuty, które mają tę samą wartość dla wszystkich instancji klas. Możesz zdefiniować atrybut klasy, przypisując wartość do nazwy zmiennej poza .__init__().
#
# class Vehicle:
#     color = "Bialy" ###przypisanie zmiennej do classy - w całej klasie bedzie to ustalona wartość
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         # self.color = 4 ### można by wprowadzić zmienną też tu ale przez self bedzie odnosił się do classy a nie do atrybutu
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# y = Bus("Man", 110, 500_000)
# z = Car("Volvo", 150, 200_000)
# print(y.name, y.color, y.mileage)
# print(z.name, z.color)

#TODO Cwiczenie 4 Utwórz podrzędną klasę Bus, która dziedziczy po klasie Vehicle. Domyślna opłata za przejazd dla dowolnego pojazdu to liczba miejsc * 100. Natomiast jeśli school_bus to instancja klasy Bus, musimy dodać dodatkowe 10% do pełnej ceny jako opłatę za utrzymanie. Tak więc łączna opłata za przejazd autobusem stanie się ostateczną kwotą = opłata całkowita + 10% ceny całkowitej.
# Uwaga: autobus może pomieścić 50 osób, więc ostateczna kwota taryfy powinna wynosić 5500. Musisz zastąpić metodę fare() klasy Vehicle w klasie Bus.
# Użyj poniższego kodu dla swojej nadrzędnej klasy Vehicle. Musimy uzyskać dostęp do klasy nadrzędnej z wnętrza metody klasy potomnej.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         # return self.capacity * 100 * 1.1 ###piersza metoda
#         return Vehicle.fare(self) * 1.1 #druga metoda z odwołaniem się do pierszej klasy Vehicle
#
#
# school_bus = Bus("Szkolne Volvo", 12, 50)
# print("Całkowita opłata za przejazd autobusem wynosi:", school_bus.fare())
# # Całkowita opłata za przejazd autobusem wynosi: 5000
# # Całkowita opłata za przejazd autobusem wynosi: 5500.0 po zmianie kodu na bus

#TODO Cwiczenie 5 Klasa Rectangle (prostokąt) i dziedziczona (podrzędna) klasa Parallelepipede (równoległościan)

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def perimeter(self):
        return 2 * (self.lenght + self.width)
    def area(self):
        return self.width * self.lenght

    def display(self):
        print(f'Width: {self.width}, Lenght {self.lenght}, Area: {self.area()}, Perimeter: {self.perimeter()}')

f=Rectangle(10,10)
f.display()

#TODO Cwiczenie 6 Utwórz klasę potomną Parallelepipede dziedziczącą po klasie Rectangle oraz z atrybutem wysokości (height) i metodą volume() w celu obliczenia objętości równoległościanu (Parallelepipede).

# class Parallelepipede(Rectangle):
#     def __init__(self, lenght, width, height):
#         self.height = height
#
#     def volume(self):
#         return Rectangle.area(self)* self.height
#
# x = Parallelepipede(2,3,4)
# x.display()
# print("Objetosc ", x.volume())

class Parallelepipede(Rectangle):
    def __init__(self,length, width, height):
        Rectangle.__init__(self,length, width)
        self.height = height
    def volume(self):
        return Rectangle.area(self)*self.height
x = Parallelepipede (5,6,7)
x.display()
print("Objętość: ", x.volume())