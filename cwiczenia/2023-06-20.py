###PETLA WHILE 20.06.2023
# liczby = list() #[]
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2  #i = i + 2
# print(liczby)  #[2, 4, 6, 8, 10]

###wykonujemy to wtedy kiedy wiemy ile razy jest proces powtarzalny
#
# lines = list()
# # print('Wprowadź tekst po linijce.')
# # print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)


# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while len(line):
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)
##STEROWANIE PTLAMI
#przerywanie


# for val in "string":
#     if val == "i":
#         break
#     print(val)
#
# print("Koniec")

###Uzycie ELSE/WHILE  z petlą for
# for i in range(1,4):
#     print(i)
# else: print("bez break")
#
# for i in range(1,4):
#     print(i)
#     break
# else: print("bez break")
###nie wykoana się else bo jest break

###SZUKAMY LICZB PIERWSZYCH
# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')

# print("kolejna lekcja wykorzystanie continue")
#
# ####CONTINUE przerywa działanie pętli i idzie do kolejnego kroku
# for num in range(1, 20):
#     if not num % 2:  # num % 2 == 0 #dzienie takie w których sprawdzamy czy jest reszta z dzielenia
#         print('Kolejna liczba parzysta:', num)
#         continue
#     print('Kolejna liczba:', num)
#
# print("kolejna lekcja wykorzystanie Pass")
# ###Pass
# for i in range(10):
#      pass
# print("Pętla wykonana")
# #TODO pass uzywany jest do zostawienia pętli z zerową wartością
#
# ##ćwiczenie 1
# Zadanie
# Napisz program, który:
# Będzie prosił użytkownika o podanie dwóch liczb, i
# Wypisze:
# Wynik ich dzielenia,
# Resztę z dzielenia, oraz
# Wynik dzielenia całkowitego
# print("Wprowadz pierwszą liczbę: ")
# liczba1=int(input)
# print("Wprowadź drugą liczbę: ")
# input=(liczba2)
# liczba1 = int
# liczba2 = int
# print("Wynik dzielenie " + liczba1/liczba2)
# print("Reszta z dzielenia "+ + liczba1%liczba2)
# print("Wynik dzielenia całkowitego " + + liczba1//liczba2)
#
###poprawne rozw
# liczba1=int(input("wprowadź pierwszą liczbę"))
# liczba2=int(input("wprowadź drugą liczbę"))
# print(liczba1/liczba2)
# print(liczba1%liczba2)
# print(liczba1//liczba2)

###PRZYKŁAD AND
# Przykład – and
# Wydrukuj True, jeśli oba stwierdzenia są prawdziwe
# x > 3 i x < 10
# Spróbuj!

# x=5
# print((x >3 and x<10))

#alternatywne rozwiazanie
# x = int(input("Wprowadz x "))
# if x>3 and x<10:
#     print("TRUE")

###przykład OR
# x = int(input("Wprowadz x "))
# print(x>4 or x<3)


#PRZYKŁAD NOT
# Przykład – not
# Odwróć wynik, wydrukuj False, jeśli wynik jest prawdziwy
# nie ( x > 3 i x < 10 )
# Spróbuj!

# x = float(input("Wprowadz x"))
#     print(not (x>3 and x<10))
#     ?????

####Cwiczenie
# Ćwiczenie instrukcji if
# Przypisz 8 do zmiennej x i 15 do zmiennej y
# Utwórz 2 instrukcje warunkowe
# Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
# Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
# Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa

# x,y = 8,15
# if (x>3 or y%2==0):
#     print("Co najmniej jeden warunek jest spełniony")
# if (x<=3 and y//2!=0):
#     print("Zaden warunek nie jest spełniony")
########
# Zadanie
# Utwórz listę zawierającą imiona: prowadzącego oraz wszystkich osób uczestniczacych w kursie
# Następnie ją posortuj alfabetycznie, oraz
# Policz ile z osób na liście jest kobietami
# W tym celu możesz sprawdzić czy imię kończy się na „a”

# lista = ['Joanna','Mikołaj','Martyna','Jakub','Marcin','Szymon']
# lista.sort()
# lista
# count_a = 0
# for x in lista:
#     if x[-1]=='a':
#         count_a+=1
# print(count_a)

#
# #####
# # Po pomyślnym wykonaniu (bez break) pętli for wyświetl komunikat „Gotowe!”
#
# for i in range(5):
#     print(i)
# else:
#     print("gotowe!")
#
# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
# z = dict(zip(keys, values))
# print(z)
#
# ###opcja 2
# # print(zip(keys, values))
# # print(list(zip(keys, values)))
#
# res_dict = dict(zip(keys, values))
# print(res_dict)
#
# ####opcja 3
# # pusty słownik
# res_dict = dict()
#
# for i in range(len(keys)):
#     res_dict.update({keys[i]: values[i]})
# # print(res_dict)
#
# # Zobaczmy ćwiczenie, które pomoże lepiej zrozumieć instrukcję PASS
# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:
#     pass
# ####musi być pass bo po else musi być cokolwiek
#
# # Znajdź liczby, które są podzielne przez 7 i są wielokrotnością 5 w zakresie
# # Napisz program w Pythonie, aby znaleźć liczby podzielne przez 7 i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)
#
# for i in range(1500,2700+1):
#     if (i%7==0 and i%5==0):
#         print(i)
#
# nl =[]
# for x in range(1500,2700+1):
#     if x%7==0 and x%5==0:
#         nl.append(str(x))
# # print(nl)
# print(";".join(nl))

###### CWICZENIE
# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for
#
# x=int(input("wprowadz x "))
# y=int(input("wprowadz y "))
# if x>=y:
#     i=y
# else:
#     i=x
# print("Niższa liczba to ", i)
# for a in range(i,0,-1):
#     if x%a==0 and y%a==0:
#         print(a)
#         break

######Wydrukuj pierwsze 10 liczb naturalnych za pomoca pętli while
# liczby = list() #[]
#  i = 10
# while i <= 11:
#     liczby.append(i)
#     i += 1  #i = i + 1
# print(liczby)
# ?????
#

# for w in range(1,6):
#     for i in range(1,w+1):
#         print(i,end=" ") ### printuje wartości i i spacje
#     print() #### przejście do nowego wiersza bo kolejna pętla
#
#
##### alternatywne rozwizanie
# c = ""
# n=5
# for i in range(1,n+1):
#     c = c + "" + str(i)
#     print(c)

#Ćwiczenie: Oblicz sumę wszystkich liczb od 1 do podanej liczby
# Napisz program akceptujący liczbę od użytkownika i obliczający sumę wszystkich liczb od 1 do podanej liczby
# Na przykład, jeśli użytkownik wpisał 10, wynik powinien wynosić 55(1+2+3+4+5+6+7+8+9+10)
# Oczekiwany wynik:
# Wpisz liczbę: 10
#
# Suma to: 55

x=int(input("wprowadz x "))
print("wynik dodawania od 1 ", x)
j=0
for i in range(1,x+1):
    j+=i
    print(i,end=" + ")
print()
print("suma = ", j)